import multiprocessing
import random

total = 1000000
n_tarefas = 20

def ponto_aleatorio():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

def multiplos_pontos(qtd_pontos):
    return sum(ponto_aleatorio() for i in range(qtd_pontos))

tamanho_tarefa = total//n_tarefas

pool = multiprocessing.Pool()
results_async = [pool.apply_async(multiplos_pontos, args=(tamanho_tarefa,)) for i in
        range(n_tarefas)]
dentro = sum(r.get() for r in results_async)

pi = 4.0 * dentro/total

print("O valor aproximado de pi é {}".format(pi))
