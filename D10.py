import time

def scheduler(f, n, *args):
    n = n/1000
    input_time = time.time()

    while time.time() < input_time + n:
        pass

    return f(*args)

scheduler(print, 5000, "hi")