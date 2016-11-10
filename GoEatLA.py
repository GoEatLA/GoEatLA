#! usr/bin/python

import threading
import time

minutes = 3

def printMsg():
	global minutes
	print (time.ctime())
	#t = threading.Timer(minutes * 60.0, printMsg)
	t = threading.Timer(minutes, printMsg)
	t.start()

printMsg()
