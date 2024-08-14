"""
READ ME:
Ignore this file.
It's used for testing certain functions, and methods.
This file holds no value to the program itself.
"""
import threading, time

done = False

def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

threading.Thread(target = worker).start()

input("Press enter to quit")
done = True