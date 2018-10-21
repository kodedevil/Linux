import os
import time

BUFFER_SIZE  = 100
PATH = "pipe"
while True:
    try:
        pipe = os.open(PATH, os.O_RDONLY | os.O_NONBLOCK)
        input = os.read(pipe, BUFFER_SIZE)
    except BlockingIOError:
        continue
    if input:
        print(input)

    os.close(pipe)

    # Other functions
    print("Sleep 500 ms")
    time.sleep(0.5)	

