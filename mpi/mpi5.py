# Versão para mpi4py de
# https://github.com/wesleykendall/mpitutorial/blob/gh-pages/tutorials/mpi-scatter-gather-and-allgather/code/avg.c

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

num_elements_per_proc = 100

rand_nums = None

if rank == 0:
    rand_nums = np.random.uniform(1, 10, [size, num_elements_per_proc])
    print("Avg of all elements is", rand_nums.mean())

sub_rand_nums = np.zeros(num_elements_per_proc)

comm.Scatter(rand_nums, sub_rand_nums, root=0)
sub_avg = sub_rand_nums.mean()

sub_avgs = None

if rank == 0:
    sub_avgs = np.zeros(size)

comm.Gather(sub_avg, sub_avgs, root=0)

if rank == 0:
    print("Avg computed across original data is", sub_avgs.mean())
