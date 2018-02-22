import multiprocessing
import random

total = 1000000

def ponto_aleatorio():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    
    if x**2 + y**2 <= 1:
        return 1
    else:
        return 0

pool = multiprocessing.Pool()
results_async = [pool.apply_async(ponto_aleatorio) for i in range(total)]
dentro = sum(r.get() for r in results_async)

pi = 4.0 * dentro/total

print("O valor aproximado de pi é {}".format(pi))
