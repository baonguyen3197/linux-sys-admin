import asyncio                              # import asyncio module

async def process_order():                  # define new coroutine
    await asyncio.sleep(1)
    print("Order completed!")

async def main():                           # define main coroutine
    await process_order()                   # await process_order coroutine
    print("All orders processed.")

asyncio.run(main())                         # start event loop
