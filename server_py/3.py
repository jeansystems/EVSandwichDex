import asyncio

async def concurrent_routine():
    # Your asynchronous code here
    await asyncio.sleep(1)
    print("Concurrent routine is done!")

async def main():
    # Create a task for the concurrent routine
    task = asyncio.create_task(concurrent_routine())

    # Run the task concurrently
    await task

asyncio.run(main())