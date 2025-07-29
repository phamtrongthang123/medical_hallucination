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

 sbatch -N1 -n24 -c1 -p condo --constraint '8a6000' -t 288:00:00 myscript.sh
