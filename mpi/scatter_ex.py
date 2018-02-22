# Use esse script com 2 tarefas MPI

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

buf_envio = None

if rank == 0:
    buf_envio = np.random.uniform(1, 10, [2, 5])
    print("Buffer de envio", buf_envio)

buf_recebimento = np.zeros(5)
print("buf_recebimento antes do Scatter", buf_recebimento, "( rank = ", rank, ")")
comm.Scatter(buf_envio, buf_recebimento, root=0)
print("buf_recebimento depois do Scatter", buf_recebimento, "( rank = ", rank, ")")
