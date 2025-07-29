import torch

attention_scores = torch.load("attention_scores.pt")

for i in range(len(attention_scores)):
    print("=========================:::",i)
    for j in range(len(attention_scores[i])):
        print(f"attention_scores[{i}][{j}] shape: {attention_scores[i][j].shape}")
