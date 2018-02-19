import multiprocessing

class Processo(multiprocessing.Process):
    
    def __init__(self, counter):
        super(Processo, self).__init__()
        self.contador = contador

    def run(self):
        for i in range(1000):
            self.contador.value += 1


contador = multiprocessing.Value('i')
contador.value = 0

processos = [Processo(contador) for i in range(4)]
[p.start() for p in processos]
[p.join() for p in processos]
print(contador.value)
