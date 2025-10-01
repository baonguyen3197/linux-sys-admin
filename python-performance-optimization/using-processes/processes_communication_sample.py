import multiprocessing
from multiprocessing import Process
from random import randint

def producer(queue):
    for i in range(10):
        queue.put(randint(1, 100))
    queue.put(None)

def consumer(queue):
    while True:
        item = queue.get()
        if item:
            print(f"Processed {item}")
        else:
            break

if __name__ == '__main__':
    queue = multiprocessing.Queue()                                 # dedicated queue

    consumer_process = Process(target=consumer, args=(queue,))      # send queue as argument

    producer_process = Process(target=producer, args=(queue,))      # send queue as argument

    consumer_process.start()                                        # start processes
    producer_process.start()

    producer_process.join()                                         # wait for processes to finish
    consumer_process.join()
    