#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH -p treinamento
#SBATCH -J hello_world

cd $SLURM_SUBMIT_DIR

source /scratch/app/modulos/intel-psxe-2016.2.062.sh
module load openmpi/2.1_intel
module load python/3.5.2

srun --mpi=pmi2 --resv-ports -n $SLURM_NTASKS python3.5 SCRIPT.py
