#!/bin/bash
#SBATCH -J medgemma
#SBATCH --nodes=1
#SBATCH --ntasks=24
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
export HOME="/scrfs/storage/tp030/home"

# Copy HF token from cache if it exists
if [ -f $HOME/.cache/huggingface/token ]; then
    export HUGGINGFACE_HUB_TOKEN=$(cat $HOME/.cache/huggingface/token)
    export HF_TOKEN=$(cat $HOME/.cache/huggingface/token)
    echo "Using HF token from cache"
else
    echo "Warning: No HF token found in cache"
fi

# Set cache directories to your accessible home directory
export HF_HOME="$HOME/.cache/huggingface"
export HUGGINGFACE_HUB_CACHE="$HOME/.cache/huggingface/hub"
export TRANSFORMERS_CACHE="$HOME/.cache/huggingface/transformers"

# Create cache directories if they don't exist
mkdir -p $HOME/.cache/huggingface/hub
mkdir -p $HOME/.cache/huggingface/transformers

CUDA_VISIBLE_DEVICES=0,1,2,3 python infer_all_mimic_eye_save_attention.py --root_dir "$HOME/mimic-eye/mimic-eye"