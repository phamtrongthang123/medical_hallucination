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
import hashlib

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
        attn_implementation="eager",
    )
    processor = AutoProcessor.from_pretrained(model_id)

    root_dir = args.root_dir
    with open('./jpg_files_list.json') as f:
        a = json.load(f)
        image_list = a['file_paths']

    results = []

    # Batch processing parameters

    def process_batch(batch_paths):
        """Process a batch of images"""
        batch_inputs_list = []

        image_path = batch_paths
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
                        "text": 'Describe the findings of the chest x-ray in a paragraph with short sentences.',
                    },
                    {"type": "image", "image": image},
                ],
            },
        ]
        question = 'Describe the findings of the chest x-ray in a paragraph with short sentences.'
        inputs = processor.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(model.device, dtype=torch.bfloat16)



        input_len = inputs["input_ids"].shape[-1]

        with torch.inference_mode():
            generation = model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False,
                output_attentions=True,
                return_dict_in_generate=True,
            )
            attention_scores = generation.attentions
            generation_ = generation.sequences[0][input_len:]

        decoded = processor.decode(generation_, skip_special_tokens=True)
        # Create unique ID from hashing image path and question
        unique_id = hashlib.md5(f"{image_path}_{question}".encode()).hexdigest()
        result = {
                "image_path": image_path,
                "question": question,
                "prediction": decoded,
                "attention_id": unique_id,
                "root": root_dir,
            }
        
        # Save attention scores for this batch
        attention_filename = f"attentions/{unique_id}.pt"
        
        # Save attention scores for this image
        torch.save(attention_scores, attention_filename)

        return [result]

    # Process images in batches
    for i in tqdm(
        range(0, len(image_list)), desc="Processing batches"
    ):
        batch_paths = image_list[i]
        batch_results = process_batch(batch_paths)
        results.extend(batch_results)

    # Save results using torch.save
    with open("result.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()