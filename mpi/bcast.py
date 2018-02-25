from mpi4py import MPI
import numpy as np

# Reimplementando Comm.Bcast com Comm.Send e Comm.Recv
#
# Os parâmetros são a informação a ser enviada (data), que processo está
# enviando (root) e qual o communicator (c)

def bcast(data, root, c):
    if c.Get_rank() == root:
        # Se sou o root, envio os dados para todo mundo
        for i in range(c.Get_size()):
            if i != root: # Não devo enviar para mim mesmo
                c.Send(data, dest = i)
    else:
        # Se sou um processo receptor, recebo as informações do root
        c.Recv(data, source = root)

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        # Fazendo o broadcast de 5 números aleatórios variando de 1 a 10
        buf_envio = np.random.uniform(1, 10, 5)
        print("Processo", rank, "/ buffer de envio", buf_envio)
        bcast(buf_envio, root=0, c=comm)
    else:
        # Inicializando o buffer de recebimento com zeros para ficar mais fácil
        # visualizar o efeito da chamada a bcast.
        buf_recebimento = np.zeros(5)
        print("Processo", rank, "/ buffer de recebimento antes do broadcast", buf_recebimento)
        bcast(buf_recebimento, root=0, c=comm)
        print("Processo", rank, "/ buffer de recebimento depois do broadcast", buf_recebimento)
