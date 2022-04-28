#!/bin/bash
#SBATCH -J train_ladino
#SBATCH -p high
#SBATCH -N 1
#SBATCH --mem=8192
#SBATCH --gres=gpu:1
#SBATCH --chdir=/homedtcl/rzevallos/TTS/slurm_jobs
#SBATCH -o slurm.%N.%J.%u.out # STDOUT
#SBATCH -e slurm.%N.%J.%u.err # STDERR

module load "Python/3.8.6-GCCcore-10.2.0"
source /homedtcl/rzevallos/TTS/virtual/bin/activate
python /homedtcl/rzevallos/TTS/TTS/recipes/ladino/train_glowtts.py
