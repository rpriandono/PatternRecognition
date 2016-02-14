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
##b = Bridge('10.10.0.100') # Enter bridge IP here. '00:17:88:15:8c:eb'

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
couchValue = mutex('off')						# Set as Global Variable
tvValue = mutex('off')
MediaValue = mutex('off')

"""
value represents:

0 = couch off, 1 = couch on, 2 = couch noisy, 3 = couch sitting, 4 = couch empty, 5 = couch lying, 
6 = tv off, 7 = tv on, 8 = tv noisy,
9 = living off, 10 = living on

"""
currentCouch = mutex(-1)
currentTV = mutex(-1)
currentLiving = mutex(-1)
currentGuard = mutex('null')
#temp1 =  sys.argv[1]							# Get port remote sensor
#port1 = int(temp1)

# Define a function for the threads


def couchProcess():
	event_pattern = []
	time.sleep(1)
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,8000))

	while 1:
		start_time = time.time()	# start time to count the execution time
		counter = 0
		while counter < 70:		# accuracy adjusment
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

		0 = couch off, 1 = couch on, 2 = couch noisy, 3 = couch sitting, 4 = couch empty, 5 = couch lying, 
		6 = tv off, 7 = tv on, 8 = tv noisy,
		9 = living off, 10 = living on
		"""

		if sitting_dist < empty_dist and sitting_dist < lying_dist and sitting_dist < light_off_dist and sitting_dist < light_on_dist and sitting_dist < noisy_dist: # and sitting_dist < quiet_dist:
			curentvalue = 3
			if curentvalue != currentCouch.content():
				print time.strftime("couch sitting - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		elif empty_dist < sitting_dist and empty_dist < lying_dist and empty_dist < light_off_dist and empty_dist < light_on_dist and empty_dist < noisy_dist: # and empty_dist < quiet_dist:
			curentvalue = 4
			if curentvalue != currentCouch.content():
				print time.strftime("couch is empty - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		elif lying_dist < sitting_dist and lying_dist < empty_dist and lying_dist < light_off_dist and lying_dist < light_on_dist and lying_dist < noisy_dist: # and lying_dist < quiet_dist:
			curentvalue = 5
			if curentvalue != currentCouch.content():
				print time.strftime("couch lying - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		elif light_off_dist < sitting_dist and light_off_dist < empty_dist and light_off_dist < lying_dist and light_off_dist < light_on_dist and light_off_dist < noisy_dist: # and light_off_dist < quiet_dist:
			curentvalue = 0
			if curentvalue != currentCouch.content():
				print time.strftime("couch light is off - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		elif light_on_dist < sitting_dist and light_on_dist < empty_dist and light_on_dist < lying_dist and light_on_dist < light_off_dist and light_on_dist < noisy_dist: # and light_on_dist < quiet_dist:
			curentvalue = 1
			if curentvalue != currentCouch.content():
				print time.strftime("couch light is on - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		elif noisy_dist < sitting_dist and noisy_dist < empty_dist and noisy_dist < lying_dist and noisy_dist < light_on_dist and noisy_dist < light_on_dist: # and noisy_dist < quiet_dist:
			curentvalue = 2
			if curentvalue != currentCouch.content():	
				print time.strftime("couch is noisy - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		else :
			print "Undefine"
			del event_pattern[:
		"""
		elif quiet_dist < sitting_dist and quiet_dist < empty_dist and quiet_dist < lying_dist and quiet_dist < light_off_dist and quiet_dist < noisy_dist and quiet_dist < light_on_dist:
			curentvalue = 'quiet'
			if curentvalue != currentCouch.content():
				print time.strftime("couch is quite - %s seconds", time.localtime(int(time.time()-start_time)))
			currentCouch.update(curentvalue)
			del event_pattern[:]
		"""
		]

def tvProcess():
	tv_event_pattern = []
	time.sleep(1)
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,8001))
	
	while 1:
		start_time = time.time()	# start time to count the execution time
		counter = 0
		while counter < 70: 		# accuracy adjusment
			datasetSensor =  connection.recv(1024)
			#print 'ERROR:', datasetSensor							# sometimes the server send nasty dataset that caused error.
			dummy = datasetSensor.strip().split('\r\n')[0]
			parts = dummy.split()
			
			if len(parts) > 1:
				event_pattern_value = float(parts[1])
				tvValue.update(event_pattern_value)
				if counter == 0:
					tv_event_pattern.append(tvValue.content())
					counter += 1
				elif tv_event_pattern[counter-1] != tvValue.content():
					tv_event_pattern.append(tvValue.content())
					counter += 1
		
		light_off_dist, light_off_cost, light_off_path = dtw(tv_light_off, tv_event_pattern)
		light_on_dist, light_on_cost, light_on_path = dtw(tv_light_on, tv_event_pattern)
		noisy_dist, noisy_cost, noisy_path = dtw(tv_noisy, tv_event_pattern)
		#quiet_dist, quiet_cost, quiet_path = dtw(tv_quiet, tv_event_pattern)

		"""
		value represents:

		0 = couch off, 1 = couch on, 2 = couch noisy, 3 = couch sitting, 4 = couch empty, 5 = couch lying, 
		6 = tv off, 7 = tv on, 8 = tv noisy,
		9 = living off, 10 = living on

		"""

		if light_off_dist < light_on_dist and light_off_dist < noisy_dist:# and light_off_dist < quiet_dist:
			curentvalue = 6
			if curentvalue != currentTV.content():
				print time.strftime("TV light is off - %s seconds", time.localtime(int(time.time()-start_time)))
			currentTV.update(curentvalue)
			del tv_event_pattern[:]
		elif light_on_dist < light_off_dist and light_on_dist < noisy_dist: # and light_on_dist < quiet_dist:
			curentvalue = 7
			if curentvalue != currentTV.content():	
				print time.strftime("Tv light is On - %s seconds", time.localtime(int(time.time()-start_time)))
			currentTV.update(curentvalue)
			del tv_event_pattern[:]
		elif noisy_dist < light_off_dist and noisy_dist < light_on_dist:# and noisy_dist < quiet_dist:
			curentvalue = 8
			if curentvalue != currentTV.content():
				print time.strftime("TV is noisy - %s seconds", time.localtime(int(time.time()-start_time)))
			currentTV.update(curentvalue)
			del tv_event_pattern[:]
		else :
			print "Undefine"
			del tv_event_pattern[:]
		
		"""
		elif quiet_dist < light_off_dist and quiet_dist < light_on_dist and quiet_dist < noisy_dist:
			curentvalue = 'quiet'
			if curentvalue != currentTV.content():
				print time.strftime("Tv is quite - %s seconds", time.localtime(int(time.time()-start_time)))
			currentTV.update(curentvalue)
			del tv_event_pattern[:]
		"""
		
def mediaProcess():
	media_event_pattern = []
	time.sleep(1)					# delay the thread for the first time.
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # connection to grab data value
	connection.connect((host,8002))

	while 1:
		start_time = time.time()	# start time to count the execution time
		counter = 0
		while counter < 70:			# accuracy adjusment
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
			curentvalue = 9
			if curentvalue != currentLiving.content():
				print time.strftime("Living room light is off - %s seconds", time.localtime(int(time.time()-start_time)))
			currentLiving.update(curentvalue)
			del media_event_pattern[:]
		elif light_on_dist < light_off_dist:
			curentvalue = 10
			if curentvalue != currentLiving.content():
				print time.strftime("Living room light is on - %s seconds", time.localtime(int(time.time()-start_time)))
			currentLiving.update(curentvalue)
			del media_event_pattern[:]
		else :
			print "Undefine"
			del media_event_pattern[:]

def PredictionThread():
	"""
	value represents:

	0 = couch off, 1 = couch on, 2 = couch noisy, 3 = couch sitting, 4 = couch empty, 5 = couch lying, 
	6 = tv off, 7 = tv on, 8 = tv noisy,
	9 = living off, 10 = living on
	"""
	history = []
	couchguard = -1
	tvguard = -1
	livingguard = -1

	preEvents = []
	predEvents = []

	print "==========Learning User behavior & Creating training datasets==========="
	# Record the user behavior
	counterLearn = 0
	while counterLearn < 250 :
		time.sleep(1)
		if currentCouch.content() != -1 or currentTV.content() != -1 or currentLiving.content() != -1:
			if couchguard != currentCouch.content():
				history.append(currentCouch.content())
				couchguard = currentCouch.content()
			elif tvguard != currentTV.content():
				history.append(currentTV.content())
				tvguard = currentTV.content()
			elif livingguard != currentLiving.content():
				history.append(currentLiving.content())
				livingguard = currentLiving.content()
		counterLearn+=1

	print "user behavior sequence :",history
	i = 1

	#Create the training dataset based on user behavior
	while i < len(history):
		if history[i] == 9:
			if history[i-2] > history[i-1]:
				preEvents.append([history[i-1], history[i-2]])
				predEvents.append(history[i])
			else:
				preEvents.append([history[i-2], history[i-1]])
				predEvents.append(history[i])
		elif history[i] == 10:
			if history[i-2] > history[i-1]:
				preEvents.append([history[i-1], history[i-2]])
				predEvents.append(history[i])
			else:
				preEvents.append([history[i-2], history[i-1]])
				predEvents.append(history[i])
		i+=1

	print "Events sequence :",preEvents
	print "Prediction result :",predEvents
	
	guard = 0

	pred = svm.SVR()
	pred.fit(preEvents, predEvents)

	print "==========Prediction==========="
	counterPred = 0
	while 1:
		time.sleep(1)
		score = round(pred.predict ([[currentCouch.content(), currentTV.content()]]))
		if score == 10:
			if guard != score:
				##lamp1.on = True
				print "Prediction : living Light On"
			guard = score
		elif score == 9:
			if guard != score:
				##lamp1.on = False
				print "Prediction : living Light Off"
			guard = score
		else:
			pass
		counterPred += 1
# Create all threads as follows

thread.start_new_thread( couchProcess, () )
thread.start_new_thread( tvProcess, () )
thread.start_new_thread( mediaProcess, () )
thread.start_new_thread( PredictionThread, () )

while 1:
   pass