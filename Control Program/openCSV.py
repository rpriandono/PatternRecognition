#!/usr/bin/python

import csv

def openFiles():

	with open('PaternDatasets/couch_empty.csv', 'rb') as csvfile:
	    couch_empty_temp = csv.reader(csvfile, delimiter=',')
	    couch_empty = []
	    for couch_empty_row in couch_empty_temp:
	        couch_empty_value = float(couch_empty_row[0])
	    	couch_empty.append(couch_empty_value)

	with open('PaternDatasets/couch_lying.csv', 'rb') as csvfile:
	    couch_lying_temp = csv.reader(csvfile, delimiter=',')
	    couch_lying = []
	    for couch_lying_row in couch_lying_temp:
	        couch_lying_value = float(couch_lying_row[0])
	    	couch_lying.append(couch_lying_value)

	with open('PaternDatasets/couch_sitting.csv', 'rb') as csvfile:
	    couch_sitting_temp = csv.reader(csvfile, delimiter=',')
	    couch_sitting = []
	    for couch_sitting_row in couch_sitting_temp:
	        couch_sitting_value = float(couch_sitting_row[0])
	    	couch_sitting.append(couch_sitting_value)

	with open('PaternDatasets/couch_light_off.csv', 'rb') as csvfile:
	    couch_light_off_temp = csv.reader(csvfile, delimiter=',')
	    couch_light_off = []
	    for couch_light_off_row in couch_light_off_temp:
	        couch_light_off_value = float(couch_light_off_row[0])
	    	couch_light_off.append(couch_light_off_value)

	with open('PaternDatasets/couch_light_on.csv', 'rb') as csvfile:
	    couch_light_on_temp = csv.reader(csvfile, delimiter=',')
	    couch_light_on = []
	    for couch_light_on_row in couch_light_on_temp:
	        couch_light_on_value = float(couch_light_on_row[0])
	    	couch_light_on.append(couch_light_on_value)

	with open('PaternDatasets/couch_noisy.csv', 'rb') as csvfile:
	    couch_noisy_temp = csv.reader(csvfile, delimiter=',')
	    couch_noisy = []
	    for couch_noisy_row in couch_noisy_temp:
	        couch_noisy_value = float(couch_noisy_row[0])
	    	couch_noisy.append(couch_noisy_value)

	with open('PaternDatasets/couch_quiet.csv', 'rb') as csvfile:
	    couch_quiet_temp = csv.reader(csvfile, delimiter=',')
	    couch_quiet = []
	    for couch_quiet_row in couch_quiet_temp:
	        couch_quiet_value = float(couch_quiet_row[0])
	    	couch_quiet.append(couch_quiet_value)

	with open('PaternDatasets/tv_light_off.csv', 'rb') as csvfile:
	    tv_light_off_temp = csv.reader(csvfile, delimiter=',')
	    tv_light_off = []
	    for tv_light_off_row in tv_light_off_temp:
	        tv_light_off_value = float(tv_light_off_row[0])
	    	tv_light_off.append(tv_light_off_value)

	with open('PaternDatasets/tv_light_on.csv', 'rb') as csvfile:
	    tv_light_on_temp = csv.reader(csvfile, delimiter=',')
	    tv_light_on = []
	    for tv_light_on_row in tv_light_on_temp:
	        tv_light_on_value = float(tv_light_on_row[0])
	    	tv_light_on.append(tv_light_on_value)

	with open('PaternDatasets/tv_noisy.csv', 'rb') as csvfile:
	    tv_noisy_temp = csv.reader(csvfile, delimiter=',')
	    tv_noisy = []
	    for tv_noisy_row in tv_noisy_temp:
	        tv_noisy_value = float(tv_noisy_row[0])
	    	tv_noisy.append(tv_noisy_value)

	with open('PaternDatasets/tv_quiet.csv', 'rb') as csvfile:
	    tv_quiet_temp = csv.reader(csvfile, delimiter=',')
	    tv_quiet = []
	    for tv_quiet_row in tv_quiet_temp:
	        tv_quiet_value = float(tv_quiet_row[0])
	    	tv_quiet.append(tv_quiet_value)

	with open('PaternDatasets/living_light_off.csv', 'rb') as csvfile:
	    living_light_off_temp = csv.reader(csvfile, delimiter=',')
	    living_light_off = []
	    for living_light_off_row in living_light_off_temp:
	        living_light_off_value = float(living_light_off_row[0])
	    	living_light_off.append(living_light_off_value)

	with open('PaternDatasets/living_light_on.csv', 'rb') as csvfile:
	    living_light_on_temp = csv.reader(csvfile, delimiter=',')
	    living_light_on = []
	    for living_light_on_row in living_light_on_temp:
	        living_light_on_value = float(living_light_on_row[0])
	    	living_light_on.append(living_light_on_value)

	return couch_empty, couch_lying, couch_sitting, couch_light_off, couch_light_on, couch_noisy, couch_quiet, tv_light_off, tv_light_on, tv_noisy, tv_quiet, living_light_off, living_light_on