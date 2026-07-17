import time


def execution_time(func):
    start = time.time()

    result = func()

    end = time.time()

    return result, round(end - start, 2)