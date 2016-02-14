#!/usr/bin/python

import thread, socket, os, datetime, sys, time
import dtw-1.0

"""
class sensorsDevice:									# Object to replace Pointer Function.
   def __init__(self, globalvalue):
      self.globalvalue = globalvalue
   
   def update(self, newValue):
   	  self.globalvalue = newValue

   def contain(self):
      return self.globalvalue

host = socket.gethostname()  							# Get local machine name							
events = sensorsDevice('?')								# Set as Global Variable
value = sensorsDevice('?')							

temp1 =  sys.argv[1]									# Get port remote sensor
temp2 =  sys.argv[2]
port1 = int(temp1)
port2 = int(temp2)
"""

# Define a function for the threads

def threadsensor():
	"""
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,port1))
	while 1:
		datasetSensor =  connection.recv(1024)
		dummy = datasetSensor.split(' ',1)
		dummy[-1] = dummy[-1].strip()
		value.update(dummy[1])
	"""
	x = [0, 0, 1, 1, 2, 4, 2, 1, 2, 0]
	y = [1, 1, 1, 2, 2, 2, 2, 3, 2, 0]

	dist, cost, path = dtw(x, y)
	print 'Minimum distance found:', dist
	
# Create all threads as follows
try:
   	thread.start_new_thread( threadsensor, () )

except:
   print "Error: unable to start thread"

while 1:
   pass
