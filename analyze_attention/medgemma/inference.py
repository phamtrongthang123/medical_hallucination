# run: time python inference.py
import snoop

snoop.install(out="debug_output.txt")


def main():
    # pip install accelerate
    import torch
    from PIL import Image
    from transformers import Gemma3ForConditionalGeneration, Gemma3Processor

    model_id = "google/medgemma-4b-it"

    model = Gemma3ForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.float32,  # Change from bfloat16 to float32 for CPU
        device_map="cpu",  # Force CPU usage
        attn_implementation="eager",
    )
    processor = Gemma3Processor.from_pretrained(model_id, use_fast=True)

    # Load your list of images
    import json
    import os

    with open("./jpg_files_list.json") as f:
        a = json.load(f)
        image_list = a["file_paths"]
        root_dir = a["root"]

    image_path = image_list[0]
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
                    "text": "Describe the findings of the chest x-ray in a paragraph with short sentences.",
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
    print(decoded) # The lungs appear clear bilaterally. There is no evidence of consolidation, effusion, or pneumothorax. The heart size is within normal limits. The mediastinal contours are unremarkable. The visualized bony structures are intact. There are no obvious acute findings.
    print(attention_scores)
    torch.save(attention_scores, 'attention_scores.pt')


if __name__ == "__main__":
    main()
