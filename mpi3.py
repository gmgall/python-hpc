import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

numero = numpy.zeros(1)

if rank == 1:
    numero = numpy.random.random_sample(1)
    print("O processo {} sorteou o número {}.".format(rank, numero[0]))
    comm.Send(numero, dest=0)

if rank == 0:
    print("O processo {} tem o número {} antes de receber o número sorteado."
        .format(rank, numero[0]))
    comm.Recv(numero, source=1)
    print("O processo {} recebeu o número {}.".format(rank, numero[0]))
