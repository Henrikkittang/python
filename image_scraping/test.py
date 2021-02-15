import concurrent.futures
import time

def multiprocessing(func):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for _ in range(10):
            executor.submit(func)

def multithreading(func):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for _ in range(10):
            executor.submit(func)

def sequential(func):
    for _ in range(10):
        func()
   
def something():
    arr = []
    for i in range(100000):
        arr.append(i)
    for _ in range(100000):
        arr.reverse()



if __name__ == '__main__':
    s = time.time()

    multithreading(something)
    
    e = time.time()
    print(e-s)


