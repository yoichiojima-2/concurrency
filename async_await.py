import asyncio
import random


async def print_number(n):
    await asyncio.sleep(random.randint(1, 3))
    print(f"done: {n}")


async def double(n):
    print(f"double: {n}")
    await asyncio.sleep(random.randint(1, 3))
    return n * 2


async def void_processing():
    print(" void start ".center(40, "-"))
    await asyncio.gather(
        print_number(1),
        print_number(2),
        print_number(3),
        print_number(4),
    )
    print(" void end ".center(40, "-"))


async def map_processing():
    print(" map start ".center(40, "-"))
    res = await asyncio.gather(*[double(n) for n in range(10)])
    print(res)
    print(" map end ".center(40, "-"))


if __name__ == "__main__":
    asyncio.run(void_processing())
    asyncio.run(map_processing())
