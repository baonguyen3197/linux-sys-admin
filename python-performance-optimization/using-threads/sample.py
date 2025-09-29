import threading                            # import the threading module

class Order(threading.Thread):              # create a subclass of Thread
    def run(self):
        print("Processing")
    
thread = Order()                            # create new instance

thread.start()                              # start the new thread

def process():                              # python function
    print("processing. . .")

t = threading.Thread(target=process)        # create new thread

t.start()                                   # start new thread
