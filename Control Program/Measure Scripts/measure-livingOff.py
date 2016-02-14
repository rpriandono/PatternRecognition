#!/usr/bin/python

import thread, socket, os, datetime, sys, time, csv, struct
sys.path.insert(0, '/home/kecap/Desktop/Control Program/dtw-1.0')
from dtw import dtw
from phue import Bridge
from openCSV import openFiles
from sklearn import svm

start_time = time.time()	# start time to count the execution time

#importing datasets pattern
couch_empty, couch_lying, couch_sitting, couch_light_off, couch_light_on, couch_noisy, couch_quiet, tv_light_off, tv_light_on, tv_noisy, tv_quiet, living_light_off, living_light_on = openFiles()
##b = Bridge('10.10.0.102') # Enter bridge IP here. '00:17:88:15:8c:eb'

##lamp1, lamp2, lamp3 = b.get_light_objects()

#Hue lamp list of colour
normal = [1,1]
red = [0.75,0.25]
purple = [0.45,0.25]
skyblue = [0.15,0.25]
blue = [0.15,0.05]
yellow = [0.45,0.51]
green = [0.09,0.81]
lightgreen = [0.3,0.5]
orange = [0.55,0.4]

start_time = time.time()	# start time for

class mutex:									# Mutex Object.
   def __init__(self, globalvalue):
      self.globalvalue = globalvalue
   
   def update(self, newValue):
   	  self.globalvalue = newValue

   def content(self):
      return self.globalvalue

host = socket.gethostname()  					# Get local machine name							
couchValue = mutex('0')							# Set as Global Variable
tvValue = mutex('0')
MediaValue = mutex('0')

"""
	value represents:
	0 = lamp off, 1 = lamp on, 2 = noisy, 3 = quite, 4 = sitting, 5 = empty, 6 = lying
"""
currentCouch = mutex(4)
currentTV = mutex(0)
currentLiving = mutex(0)

#temp1 =  sys.argv[1]							# Get port remote sensor
#port1 = int(temp1)

# Define a function for the threads

def mediaProcess():
	media_event_pattern = []
	time.sleep(1)					# delay the thread for the first time.
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,6001))
	chunk = 1
	sample = 1
	
	while chunk <= 100:
		TP = 0
		waktu = 0
		while sample <= 100:
			start_time = time.time()	# start time to count the execution time
			counter = 0
			while counter < chunk:			# accuracy adjusment
				datasetSensor =  connection.recv(1024)
				#print 'ERROR:', datasetSensor							# sometimes the server send nasty dataset that caused error.
				dummy = datasetSensor.strip().split('\r\n')[0]
				parts = dummy.split()
				
				if len(parts) > 1:
					event_pattern_value = float(parts[1])
					MediaValue.update(event_pattern_value)
					if counter == 0:
						media_event_pattern.append(MediaValue.content())
						counter += 1
					elif media_event_pattern[counter-1] != MediaValue.content():
						media_event_pattern.append(MediaValue.content())
						counter += 1
					
			light_off_dist, light_off_cost, light_off_path = dtw(living_light_off, media_event_pattern)
			light_on_dist, light_on_cost, light_on_path = dtw(living_light_on, media_event_pattern)

			if light_off_dist < light_on_dist:
				currentLiving.update(0)
				#print time.strftime("Living room light is off - %s seconds", time.localtime(int(time.time()-start_time)))
				
				TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del media_event_pattern[:]
			elif light_on_dist < light_off_dist:
				currentLiving.update(1)
				#print time.strftime("Living room light is on - %s seconds", time.localtime(int(time.time()-start_time)))
				
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del media_event_pattern[:]
			else :
				print "Undefine"
				del media_event_pattern[:]		
		print "LivingOff,",chunk,",",TP,",",waktu/100
		sample = 1
		chunk += 1

# Create all threads as follows

thread.start_new_thread( mediaProcess, () )


while 1:
   pass