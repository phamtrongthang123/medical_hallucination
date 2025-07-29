#!/bin/bash
#SBATCH -J medgemma
#SBATCH --nodes=1
#SBATCH --ntasks=192
#SBATCH --cpus-per-task=1
#SBATCH --partition=condo
#SBATCH --constraint='8a6000'
#SBATCH --time=12-00:00:00
#SBATCH -o slurm_log/medgemma_%j.txt
#SBATCH -e slurm_log/medgemma_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=tp030@uark.edu

export OMP_NUM_THREADS=1

module load python/anaconda-3.14
conda activate /scrfs/storage/tp030/home/.conda/envs/medgemma/

# Copy HF token from cache if it exists
if [ -f /scrfs/storage/tp030/home/.cache/huggingface/token ]; then
    export HUGGINGFACE_HUB_TOKEN=$(cat /scrfs/storage/tp030/home/.cache/huggingface/token)
    export HF_TOKEN=$(cat /scrfs/storage/tp030/home/.cache/huggingface/token)
    echo "Using HF token from cache"
else
    echo "Warning: No HF token found in cache"
fi

# Set cache directories to your accessible home directory
export HF_HOME="/scrfs/storage/tp030/home/.cache/huggingface"
export HUGGINGFACE_HUB_CACHE="/scrfs/storage/tp030/home/.cache/huggingface/hub"
export TRANSFORMERS_CACHE="/scrfs/storage/tp030/home/.cache/huggingface/transformers"

# Create cache directories if they don't exist
mkdir -p /scrfs/storage/tp030/home/.cache/huggingface/hub
mkdir -p /scrfs/storage/tp030/home/.cache/huggingface/transformers


python infer_all_mimic_eye.py --root_dir "~/mimic-eye"