import multiprocessing

class Processo(multiprocessing.Process):
    
    def __init__(self, contador):
        super(Processo, self).__init__()
        self.contador = contador

    def run(self):
        for i in range(1000):
            self.contador.value += 1


var_compartilhada = multiprocessing.Value('i')
var_compartilhada.value = 0

processos = [Processo(var_compartilhada) for i in range(4)]
[p.start() for p in processos]
[p.join() for p in processos]
print(var_compartilhada.value)
