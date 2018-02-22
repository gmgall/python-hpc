import pycuda.driver as drv

drv.init()
print("{} dispositivos encontrados.".format(drv.Device.count()))

for ordinal in range(drv.Device.count()):
    dev = drv.Device(ordinal)
    print("Dispositivo {}: {}".format(ordinal, dev.name()))
    print("	Capacidades", dev.compute_capability())
    print("	Memória total: {} KB".format(dev.total_memory()//1024))
