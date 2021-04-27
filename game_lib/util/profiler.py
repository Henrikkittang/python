import functools
import time
import numpy as np

def timer(func: callable) -> callable:
    functools.wraps(func)
    def inner(*args, **kwargs) -> callable:
        timeStart = time.time()
        value = func(*args, **kwargs)
        timeEnd = time.time()
        print(f"function '{func.__name__}' took {timeEnd-timeStart} seconds")
        return value
    return inner

def repeat(iterations:int) -> callable:
    def decorator(func) -> callable:
        def wrapper(*args, **kwargs) -> any:
            for _ in range(iterations-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def average_time(iterations:int) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs) -> any:
            arr = np.zeros(iterations)
            value = None
            for idx in range(iterations):
                timeStart = time.time()
                value = func(*args, **kwargs)
                timeEnd = time.time()
                arr[idx] = timeEnd-timeStart
            print(f"function '{func.__name__}' average time over {iterations} iterations is {np.average(arr)} seconds")
            return value
        return wrapper
    return decorator



def mean_time(iterations:int) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs) -> any:
            arr = np.zeros(iterations)
            value = None
            for idx in range(iterations):
                timeStart = time.time()
                value = func(*args, **kwargs)
                timeEnd = time.time()
                arr[idx] = timeEnd-timeStart
            print(f"function '{func.__name__}' mean time over {iterations} iterations is {np.mean(arr)} seconds")
            return value
        return wrapper
    return decorator

@mean_time(iterations=2)
def fun(secs):
    time.sleep(secs)

fun(0.2)

