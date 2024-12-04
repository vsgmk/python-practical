import threading
import time

def print_number():
    for i in range(0,5):
        time.sleep(1)
        print(f"Number: {i}")

def print_char():
    for letter in ['A','B','C','D','E']:
        time.sleep(1)
        print(f"Character: {letter}")

thread1 = threading.Thread(target=print_number)
thread2 = threading.Thread(target=print_char)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Completed the threads")
