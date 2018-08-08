#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -p treinamento
#SBATCH -J hello_world
#SBATCH --exclusive

cd $SLURM_SUBMIT_DIR

source /scratch/app/modulos/intel-psxe-2017.sh
module load openmpi/2.1_intel
module load python/3.5.2

bash -c 'time python3.5 SCRIPT.py'
