# Creating Mamba Environment with UV and Scientific Packages

```bash
# Create new environment
mamba create -n scientific_env python=3.10

# Activate the environment
mamba activate scientific_env

# Install UV package manager
pip install uv

# Install essential scientific packages
uv pip install numpy \
    pandas \
    scipy \
    matplotlib \
    scikit-learn \
    jupyter \
    seaborn

# Install additional dependencies using UV (faster than pip)
uv pip install \
    statsmodels \
    plotly
```

```bash
# Install machine learning and deep learning packages
uv pip install einops==0.6.1 \
    einops-exts==0.0.4 \
    fastapi \
    gradio==3.35.2 \
    gradio_client==0.2.9 \
    markdown2[all] \
    numpy==1.26.0 \
    requests \
    sentencepiece==0.1.99 \
    tokenizers>=0.12.1 \
    torch==2.0.1 \
    torchvision==0.15.2 \
    uvicorn \
    wandb \
    shortuuid \
    httpx==0.24.0 \
    deepspeed==0.9.5 \
    peft==0.4.0 \
    transformers==4.31.0 \
    accelerate==0.21.0 \
    bitsandbytes==0.41.0 \
    scikit-learn==1.2.2 \
    open-clip-torch==2.23.0 \
    timm==0.9.12 \
    fire \
    evaluate \
    radgraph==0.0.9 \
    rouge_score \
    statsmodels \
    sacrebleu
```