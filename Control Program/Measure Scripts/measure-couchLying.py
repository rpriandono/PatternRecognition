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

def couchProcess():
	event_pattern = []
	time.sleep(1)
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,8003))
	chunk = 1
	sample = 1

	while chunk <= 100:
		TP = 0
		waktu = 0
		while sample <= 100:
			start_time = time.time()	# start time to count the execution time
			counter = 0
			while counter < chunk:		# accuracy adjusment
				datasetSensor =  connection.recv(1024)
				#print 'ERROR:', datasetSensor							# sometimes the server send nasty dataset that caused error.
				dummy = datasetSensor.strip().split('\r\n')[0]
				parts = dummy.split()
				
				if len(parts) > 1:
					#try:
					event_pattern_value = float(parts[1])
					#except:
					#	print 'ERROR:', parts
					couchValue.update(event_pattern_value)
					if counter == 0:
						event_pattern.append(couchValue.content())
						counter += 1
					elif event_pattern[counter-1] != couchValue.content():
						event_pattern.append(couchValue.content())
						counter += 1
				
			sitting_dist, sitting_cost, sitting_path = dtw(couch_sitting, event_pattern)
			empty_dist, empty_cost, empty_path = dtw(couch_empty, event_pattern)
			lying_dist, lying_cost, lying_path = dtw(couch_lying, event_pattern)
			light_off_dist, light_off_cost, light_off_path = dtw(couch_light_off, event_pattern)
			light_on_dist, light_on_cost, light_on_path = dtw(couch_light_on, event_pattern)
			noisy_dist, noisy_cost, noisy_path = dtw(couch_noisy, event_pattern)
			quiet_dist, quiet_cost, quiet_path = dtw(couch_quiet, event_pattern)
			
			"""
			value represents:
			0 = lamp off, 1 = lamp on, 2 = noisy, 3 = quite, 4 = sitting, 5 = empty, 6 = lying
			"""

			if sitting_dist < empty_dist and sitting_dist < lying_dist and sitting_dist < light_off_dist and sitting_dist < light_on_dist and sitting_dist < noisy_dist and sitting_dist < quiet_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif empty_dist < sitting_dist and empty_dist < lying_dist and empty_dist < light_off_dist and empty_dist < light_on_dist and empty_dist < noisy_dist and empty_dist < quiet_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif lying_dist < sitting_dist and lying_dist < empty_dist and lying_dist < light_off_dist and lying_dist < light_on_dist and lying_dist < noisy_dist and lying_dist < quiet_dist:
				TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif light_off_dist < sitting_dist and light_off_dist < empty_dist and light_off_dist < lying_dist and light_off_dist < light_on_dist and light_off_dist < noisy_dist and light_off_dist < quiet_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif light_on_dist < sitting_dist and light_on_dist < empty_dist and light_on_dist < lying_dist and light_on_dist < light_off_dist and light_on_dist < noisy_dist and light_on_dist < quiet_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif noisy_dist < sitting_dist and noisy_dist < empty_dist and noisy_dist < lying_dist and noisy_dist < light_on_dist and noisy_dist < light_on_dist and noisy_dist < quiet_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			elif quiet_dist < sitting_dist and quiet_dist < empty_dist and quiet_dist < lying_dist and quiet_dist < light_off_dist and quiet_dist < noisy_dist and quiet_dist < light_on_dist:
				#TP += 1
				sample += 1
				waktu = waktu + int(time.strftime("%s", time.localtime(int(time.time()-start_time))))
				del event_pattern[:]
			else :
				print "Undefine"
				del event_pattern[:]
		print "couch_lying,",chunk,",",TP,",",waktu/100
		sample = 1
		chunk += 1
		
# Create all threads as follows

thread.start_new_thread( couchProcess, () )

while 1:
   pass