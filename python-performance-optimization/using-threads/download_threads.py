from urllib import request
import threading

def download():
    return request.urlopen('https://google.com').read()

def single_thread():
    for _ in range(5):
        download()

def multiple_thread():
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=download))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

@profile
def main():
    single_thread()
    multiple_thread()

main()