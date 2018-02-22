#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -p treinamento_gpu
#SBATCH -J hello_world
#SBATCH --exclusive

module load cuda/8.0
module load python/3.5.2

python3.5 pyCUDA2.py
