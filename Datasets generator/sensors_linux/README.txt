#
# Sensors
#
# Version 0.4
#
# Copyright Mike Holenderski
# Contact mike@holenderski.com
#

Sensors simulates a set of virtual sensors and provides their data stream over
TCP sockets, with each sensor listening on its own port.

You can start the application by executing it in a terminal in the directory
contianing the executable.


Usage: sensors ?options? config

Required:
config : Path to the configuration file specifying the sensor properties.
         
Options:
--control number : Port number for accepting control commands. (Default '')
                   
