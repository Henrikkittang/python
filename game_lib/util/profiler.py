import cProfile
import pstats
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


def file_profile(maxLineNumber:int=15) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs) -> any:
            filename = 'profile-'  + func.__name__
            cProfile.run(func.__name__, filename)

            with open(filename + '.txt', 'w') as file:
                profile = pstats.Stats('./' + filename, stream=file)
                profile.sort_stats('cumulative') 
                profile.print_stats(maxLineNumber)
                file.close()
        return wrapper
    return decorator






