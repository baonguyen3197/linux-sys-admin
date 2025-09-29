import asyncio

async def process_order():
    await asyncio.sleep(5)
    print("Order completed!")

async def main():
    await asyncio.gather(process_order(), process_order())
    print("All orders processed.")

asyncio.run(main())