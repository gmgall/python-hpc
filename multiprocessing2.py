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
    p = Processo(0)
    p.start()
    p.join()
    print("Sou o processo mestre")
