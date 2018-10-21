import os
import time

PATH = "pipe"

while True:
    with os.fdopen(os.open(PATH, os.O_RDONLY | os.O_NONBLOCK)) as pipe:
        received = pipe.read()
        if received:
            print("Read: '{}'".format(received))
    print("Sleep 500 ms")
    time.sleep(0.5)

