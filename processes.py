import time
import random
from concurrent.futures import ProcessPoolExecutor


def print_number(n):
    print(f"invoked: {n}")
    time.sleep(random.randint(1, 3))
    print(f"done: {n}")


def void_processing():
    print(" void start ".center(40, "-"))

    with ProcessPoolExecutor() as executor:
        executor.submit(print_number, 1)
        executor.submit(print_number, 2)
        executor.submit(print_number, 3)
        executor.submit(print_number, 4)

    print(" void end ".center(40, "-"))


def double(n):
    print(f"invoked: {n}")
    time.sleep(random.randint(1, 3))
    return n * 2


def map_processing():
    print(" map start ".center(40, "-"))

    with ProcessPoolExecutor() as executor:
        res = executor.map(double, range(10))

    print(list(res))
    print(" map end ".center(40, "-"))


if __name__ == "__main__":
    s = time.time()
    void_processing()
    map_processing()
    e = time.time()
    print(f"took: {e - s} s")
