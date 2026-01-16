import threading
import time

lock=threading.Lock()
def square(num):
    with lock:
        print(f"square is {num*num}")
        time.sleep(6)

def cube(num):
    print(f"cube is {num*num*num}")
    time.sleep(6)

t1=threading.Thread(target=square,args=(4,))
t2=threading.Thread(target=cube,args=(4,))

t1.start()
t2.start()
t1.join()
t2.join()

print("done")