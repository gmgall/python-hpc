import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
        
    inputs = [0, 1, 2, 3, 4]
    outputs = pool.map(square, inputs)
    print(outputs)
