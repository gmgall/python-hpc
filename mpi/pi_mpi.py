from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

import numpy as np

total = 100000000

n_procs = comm.Get_size()

print("Esse é o processo", rank)

# Create an array
x_parcial = np.random.uniform(-1, 1, int(total/n_procs))
y_parcial = np.random.uniform(-1, 1, int(total/n_procs))

dentro_parcial = x_parcial**2 + y_parcial**2 <= 1
dentro_parcial_soma = dentro_parcial.sum()

print("Contagem parcial de pontos dentro do círculo:", dentro_parcial_soma)

contagem_final = comm.reduce(dentro_parcial_soma, op=MPI.SUM, root=0)

if rank == 0:
    print("Contagem final de pontos dentro do círculo:", contagem_final)
    print("Aproximação de pi:", 4 * contagem_final/total)
