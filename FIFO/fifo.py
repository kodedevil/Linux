import os
import errno

path = "pipe";	#path to the pipe used for accessing serial communication

while 1:
	pipe = os.open(path, os.O_RDONLY | os.O_NONBLOCK);
	try:
		input = os.read(pipe,10);
	except OSError as err:
		if err.errno == 11:
			import time
			time.sleep(0)
		else:
			raise err;

	if input:
		print(input[0]);
		
	os.close(pipe);
