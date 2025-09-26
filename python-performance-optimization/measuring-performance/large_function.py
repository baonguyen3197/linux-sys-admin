import time

@profile
def heavy_work():
    print("Do some heavy work")
    print("Do some heavy work")
    print("Do some heavy work")
    for _ in range(1_000_000):
        pass
    print("Do some heavy work")
    print("Do some heavy work")

start_time = time.time()
heavy_work()
end_time = time.time()
print(f"Duration: {end_time - start_time} seconds")