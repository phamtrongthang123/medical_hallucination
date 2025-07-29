```bash
mamba create -n medgemma python=3.10
mamba activate medgemma

pip install uv 
uv pip install -U transformers torch torchvision
uv pip install accelerate 
```

```bash
CUDA_VISIBLE_DEVICES=0 python medgemma_example.py
CUDA_VISIBLE_DEVICES=0 python infer_all_mimic_eye.py
```