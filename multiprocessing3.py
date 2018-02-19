import multiprocessing
import time

class Processo(multiprocessing.Process):
    def __init__(self, id):
        super(Processo, self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("Sou o processo com ID: {}".format(self.id))

if __name__ == '__main__':
    processes = Processo(1), Processo(2), Processo(3), Processo(4)
    [p.start() for p in processes]
    print("Sou o processo mestre")
