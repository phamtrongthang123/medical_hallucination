# pip install accelerate
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import requests
import torch

model_id = "google/medgemma-27b-it"

model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)

from tqdm import tqdm 
# Load your list of images
import json 
with open('./jpg_files_list.json') as f:
    a = json.load(f)
    image_list = a['file_paths']
    root_dir = a['root']

import os 
results = [] 

# Batch processing parameters
batch_size = 10  # Adjust based on your GPU memory

def process_batch(batch_paths):
    """Process a batch of images"""
    batch_inputs_list = []
    
    for image_path in batch_paths:
        image = Image.open(os.path.join(root_dir, image_path))
        
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are an expert radiologist."}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Provide a description of the findings in the radiology image"},
                    {"type": "image", "image": image}
                ]
            }
        ]
        
        inputs = processor.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=True,
            return_dict=True, return_tensors="pt"
        ).to(model.device, dtype=torch.bfloat16)
        
        batch_inputs_list.append(inputs)
    
    # Simple concatenation along batch dimension
    # All inputs should have the same keys from apply_chat_template
    batch_inputs = {}
    for key in batch_inputs_list[0].keys():
        batch_inputs[key] = torch.cat([inp[key] for inp in batch_inputs_list], dim=0)
    
    input_len = batch_inputs_list[0]["input_ids"].shape[-1]
    
    with torch.inference_mode():
        generation = model.generate(
            **batch_inputs, 
            max_new_tokens=200, 
            do_sample=False
        )
        generation = generation[:, input_len:]
    
    # Decode each result
    batch_results = []
    for i, gen in enumerate(generation):
        decoded = processor.decode(gen, skip_special_tokens=True)
        batch_results.append({
            'image_path': batch_paths[i], 
            'prediction': decoded, 
            'root': root_dir
        })
    
    return batch_results

# Process images in batches
for i in tqdm(range(0, len(image_list), batch_size), desc="Processing batches"):
    batch_paths = image_list[i:i + batch_size]
    batch_results = process_batch(batch_paths)
    results.extend(batch_results)

with open('result.json', 'w') as f:
    json.dump(results, f, indent=4)