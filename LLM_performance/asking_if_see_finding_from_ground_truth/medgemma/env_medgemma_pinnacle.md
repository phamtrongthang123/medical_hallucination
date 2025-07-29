```bash
conda create -n medgemma python=3.10
conda activate medgemma

pip install uv 
uv pip install -U transformers torch torchvision
uv pip install accelerate 
```

```bash
python infer_all_mimic_eye.py
```