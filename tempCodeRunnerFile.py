import threading
import time

def fun(i,j):
    for i in range(i,j):
        print("Hi")
        time.sleep(1)

thread=threading.Thread(target=fun, args=(4,6))
thread.start()
