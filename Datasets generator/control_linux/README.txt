#
# Control
#
# Version 0.4
#
# Copyright Mike Holenderski
# Contact mike@holenderski.com
#

Control connects to a virtual sensor server and provides a user interface for
trigerring events on that server. The list of available events is retrieved
from the server and a button is created for each one.

You can start the application by executing it in a terminal in the directory
contianing the executable.


Usage: control ?options? host port

Required:
host : Host name or IP adddress of the server.
       
port : Control port on which the server is listening.
       
Options:
--events list : List of events that can be generated, e.g. "hot warm cold". If
                this argument is omitted then a list of all possible events is
                retrieved from the server. (Default '')
                
