import time
from datetime import datetime
import threading

def schedule(f, n, args=None):
    """
    Spawn a thread with function
    execute and pass f, n and args
    as arguments.
    """
    t = threading.Thread(target=execute, args=(f, n, args))
    t.start()
    print("Started:", t.name)

def execute(f, n, args=None):
    """
    Execute f after n milliseconds
    with optional args as arguments
    for f.
    """
    seconds = n / 1000
    time.sleep(seconds)

    if args is None:
        f()
    else:
        f(*args)

def print_time():
    """
    A simple function which
    prints the current time.
    """
    current_time = datetime.now()
    print("Time:", current_time)

def sum(a, b):
    """
    A simple function which
    prints the sum of a and b.
    """
    sum = a + b
    print("{a} + {b} =".format(a=a, b=b), sum)

if __name__ == "__main__":
    schedule(sum, 1000, (10, 10))
    schedule(print_time, 5000)