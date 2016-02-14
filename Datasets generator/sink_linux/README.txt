#
# Sink
#
# Version 0.4
#
# Copyright Mike Holenderski
# Contact mike@holenderski.com
#

Sink connects to a virtual sensor over a TCP socket, and visualizes the incoming
streaming data.

You can start the application by executing it in a terminal in the directory
contianing the executable.


Usage: sink ?options? host port

Required:
host : Host name or IP adddress of the server.
       
port : Port on which the sensor is listening.
       
Options:
--speed number       : Scroll speed, in pixels per second. (Default 50)
                       
--refreshRate number : Screen refresh rate (the entire screen is redrawn at this
                       rate). (Default 40)
                       
--print 1 | 0        : Print the incoming data to the standard output. (Default
                       0)
                       
--plot 1 | 0         : Visualize the incoming data on a 2D plot. (Default 1)
                       
