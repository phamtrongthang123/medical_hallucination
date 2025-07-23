import json

def update_predictions():
    # Load File A (Gemma results) - JSON format
    with open('result.json', 'r') as f:
        gemma_results = json.load(f)
    
    # Create a mapping from image ID to prediction
    # Extract ID from image_path (assuming ID is the filename without extension)
    id_to_prediction = {}
    for item in gemma_results:
        image_path = item['image_path']
        # Extract the image filename (without .jpg extension) as ID
        image_filename = image_path.split('/')[-1]  # Get filename
        image_id = image_filename.replace('.jpg', '')  # Remove extension
        id_to_prediction[image_id] = item['prediction']
    
    # Load File B (ChatGPT format) - JSONL format
    updated_items = []
    with open('../chatgpt/prediction.jsonl', 'r') as f:
        for line in f:
            item = json.loads(line.strip())
            item_id = item['id']
            
            # Find matching prediction from Gemma results
            # Check if any image ID contains the item_id as substring
            found_prediction = None
            for gemma_id, prediction in id_to_prediction.items():
                if item_id in gemma_id:
                    found_prediction = prediction
                    break
            
            # Update prediction if found
            if found_prediction:
                item['prediction'] = found_prediction
                print(f"Updated prediction for ID: {item_id}")
            else:
                print(f"No matching prediction found for ID: {item_id}")
            
            updated_items.append(item)
    
    # Save updated results
    with open('updated_prediction.jsonl', 'w') as f:
        for item in updated_items:
            f.write(json.dumps(item) + '\n')
    
    print(f"Updated {len(updated_items)} items and saved to 'updated_prediction.jsonl'")

if __name__ == "__main__":
    update_predictions()