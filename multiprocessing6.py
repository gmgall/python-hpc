import multiprocessing

def square(x):
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
        
    results_async = [pool.apply_async(square, args=(i,)) for i in range(100)]
    results = [r.get() for r in results_async]
    print(results)
