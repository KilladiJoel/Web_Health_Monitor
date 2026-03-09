import asyncio
import time

async def say_hello(name: str, delay: int):
    await asyncio.sleep(delay)
    print(f"Finished {name} after {delay} seconds")

async def main():
    start = time.perf_counter()
    
    # This fires BOTH tasks at the same time
    await asyncio.gather(
        say_hello("Task A", 3),
        say_hello("Task B", 3)
    )
    
    end = time.perf_counter()
    print(f"Total time taken: {end - start:.2f} seconds")

asyncio.run(main())