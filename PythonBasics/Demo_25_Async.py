"""
By default python is synchronous and will have sequential execution
Also it has ability to make asynchronous

Synchronous - code runs one by one line
Asynchronous - all lines executed concurrently should provide async keyword to wait for another line to complete

"""
import asyncio
import time


def task(name):
    print(f"Starting task for {name}")
    time.sleep(2)
    print(f"Finishing task for {name}")

task("Subba")
task("Rao")

async def task(name):
    print(f"Starting task for {name}")
    await asyncio.sleep(2) # when first function is in wait mode 2nd function started immediately
    print(f"Finishing task for {name}")

async def main():
    await asyncio.gather(task("Rahul"), task("Setty"))# gather tasks for concurrent run

asyncio.run( main() )