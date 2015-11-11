import os
import errno
import time

bufferSize = 100;
PATH = "pipe";
while 1:
	try:
		pipe = os.open(PATH, os.O_RDONLY | os.O_NONBLOCK);
		input = os.read(pipe,bufferSize);
	except OSError as err:
		if err.errno == 11:
			continue;
		else:
			raise err;
	if input:
		print(input);

    os.close(pipe);

    #Other functions
    print "Sleep 500 ms"
    time.sleep(0.5);	
