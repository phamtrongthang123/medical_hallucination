# pip install accelerate
# Load your list of images
import json
import os
import sys
import argparse

import torch
from PIL import Image
from tqdm import tqdm
from transformers import AutoModelForImageTextToText, AutoProcessor

def main():
    parser = argparse.ArgumentParser(description="Process MIMIC-Eye images with MedGemma")
    parser.add_argument(
        "--root_dir", 
        type=str, 
        default="/scr/thang._./mimic-eye/mimic-eye-integrating-mimic-datasets-with-reflacx-and-eye-gaze-for-multimodal-deep-learning-applications-1.0.0/mimic-eye",
        help="Root directory path for MIMIC-Eye dataset"
    )
    args = parser.parse_args()

    model_id = "google/medgemma-27b-it"

    model = AutoModelForImageTextToText.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    processor = AutoProcessor.from_pretrained(model_id)

    root_dir = args.root_dir
    with open("./dicom_question_pairs.json") as f:
        image_question_pairs = json.load(f)

    results = []

    # Batch processing parameters
    batch_size = 1  # the question length will be different, and i don't know what to pad here. I chose the safer way: set batch = 1 

    def process_batch(batch_paths):
        """Process a batch of images"""
        batch_inputs_list = []

        for image_path, question in batch_paths:
            image = Image.open(os.path.join(root_dir, image_path))

            messages = [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": "You are an expert radiologist."}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question,
                        },
                        {"type": "image", "image": image},
                    ],
                },
            ]

            inputs = processor.apply_chat_template(
                messages,
                add_generation_prompt=True,
                tokenize=True,
                return_dict=True,
                return_tensors="pt",
            ).to(model.device, dtype=torch.bfloat16)

            batch_inputs_list.append(inputs)

        # Simple concatenation along batch dimension
        # All inputs should have the same keys from apply_chat_template
        batch_inputs = {}
        for key in batch_inputs_list[0].keys():
            
            batch_inputs[key] = torch.cat([inp[key] for inp in batch_inputs_list], dim=0)

        input_len = batch_inputs_list[0]["input_ids"].shape[-1]

        with torch.inference_mode():
            generation = model.generate(**batch_inputs, max_new_tokens=200, do_sample=False)
            generation = generation[:, input_len:]

        # Decode each result
        batch_results = []
        for i, gen in enumerate(generation):
            decoded = processor.decode(gen, skip_special_tokens=True)
            batch_results.append(
                {
                    "image_path": batch_paths[i][0],
                    "question": batch_paths[i][1],
                    "prediction": decoded,
                    "root": root_dir,
                }
            )

        return batch_results

    # Process images in batches
    for i in tqdm(
        range(0, len(image_question_pairs), batch_size), desc="Processing batches"
    ):
        batch_paths = image_question_pairs[i : i + batch_size]
        batch_results = process_batch(batch_paths)
        results.extend(batch_results)

    with open("result.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()