# PatternRecognition
In order to execute our program on Linux, proceed as follows:

1. 	Make sure to have Python version 2.7.9 installed for Linux; you can download it from the Python website https://www.python.org/downloads/release/python-279/
2.	Make sure to have the Python scikit library installed for Linux; you can download it and follow the installation instructions on http://scikit-learn.org/stable/install.html
3.	Open the Python program, located in the Control Program directory, in a text editor. You need to change the path to the DTW library, to make sure it can find it. The required line currently looks like this:
		sys.path.insert(0, '/home/kecap/Desktop/Control Program/dtw-1.0')
	Replace the first part of the path (/home/kecap/Desktop/) to the directory where this submission folder is extracted.
4. 	Open two separate Unix shells.
5. 	In the first shell, navigate to the Datasets generator/sensors_linux directory (make sure you are inside this directory) and type the following line in the shell:
		./sensors --control 6666 Prediction-Demo.sens
	do NOT press Enter yet.
6. 	In the second shell, navigate to the Control program directory (make sure you are inside this directory) and type the following line in the shell:
		python prediction.py
	do NOT press Enter yet.
7. 	In order for our program to work correctly, the commands from step 5 and 6 need to be executed very quickly one after the other, starting with the command in step 5. To achieve this, make sure that both shells from step 5 and 6 are visible (and the above lines are already typed). Switch to the first shell and press Enter and immediately hereafter, switch to the second shell and press Enter again. The sensor server and our program are now running.
8.	To allow generating events manually, open a third shell and navigate to the controller_linux subdirectory (make sure you are inside this directory). Execute the following line in the shell:
		./control localhost 6666
	This will open a new window with many buttons. Each button represents an event that can be generated at the server.
	
Our program will print its status on the command line, in order to indicate its state. After the observing and learning phase, our program goes into a prediction phase, where it will print which events it has classified and which prediction it makes for these classified events. During this last phase, the controller that was started in line 6 can be used to test our program. In our event schedule from line 1, a couch and TV event is always followed by a living light event. Hence, if one presents our program with the preceeding couch and TV event (by pressing the buttons from the controller), our program should predict the corresponding living light event.

NOTE: in order to prevent the shells from being flooded with printed lines, our program will only print the classified and predicted events if they are different from the ones it printed last. Therefore, it might seem as if our program gives no response when it is presented with a couch and TV event that gives rise to the same living light event (for instance, living_light_off). In order to test it properly, we propose to alternate couch and TV events that lead to living_light_on and living_light_off.
