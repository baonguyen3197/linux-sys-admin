from multiprocessing import Process         # import the multiprocessing module

class OrderProcessing(Process):             # create a subclass of Process
    def run(self):
        print(f"Processing")

process = OrderProcessing()                 # create new instance
process.start()                             # start new process

def process_order():                        # python function
    print(f"Processing. . .")

p = Process(target=process_order)           # create new process
p.start()                                   # start new process