**Daemon script to feed ISKRA ME162 data to Domoticz**
===================================================

This python script can run as a daemon and reads the usage data from an
ISKRA ME162 (will most likely work for other digital meters that have
an iec62056-21 interface too.

**Requirements**
------------
Python3 

**Usage:**
------
*iskra-me162*

**Configuration**
-------------
The package installs a configuration file in /etc/default/iskra-me162.
This file looks like:

::

	# Settings for the domoticz server

	domoticzserver="domoticz.home.fazant.net:8080"
	domoticzusername = "XXXXX"
	domoticzpassword = "XXXXXXXX"
	device_index = 54

	# port for ir-head

	port = "/dev/ttyUSB0"

	# use high speed: switch to high speed reading, may not work
	# Set True or False
	use_highspeed = False

	# print debug information?
	# 0 = no debug information printed
	# 1 = normal debug information printed
	# 2 = detailed information printed
	print_debug = 0

	# state file is often written, so on a raspberry pi make sure it
	# is on a memory back file system (tmpfs)
	state_file = "/var/run/me162-state"

	# interval for updating domoticz, recommend at least 60 seconds
	update_interval = 120

**Description of the options in the configuration file**
-----------------------------------------------------

The settings for the domoticz server are pretty simple.
The script expects a dummy device of type "Dummy". Click then the
"create virtual sensors" button and select the "P1 smart meter (electric)" 
type for the virtual sensor.
In the Setup->Devices tab look for the new device and note the Idx value
allocated to the sensor. Edit the configuration file device_index to match 
the new device index. 

If your IR-head is connected to a different serial port, edit the port value.

Print_debug will enable debug printouts from the script so you can see what
happens.See the configuration file for a description of the possible values.

The script needs to maintain some state of the latest values sent to domoticz.
In order not to wear out the sd-card it is recommended to store the file on 
a tmpfs filesystem.

The script is meant to be run  as a daemon. The update-interval determines
the frequency of updating Domoticz.

**Known problems**
--------------
The use_highspeed option, used to control the speed of the serial connection
does not always work. As the amount of data to be transferred is fairly small
I leave the serial speed at 300 baud (use_highspeed = False) so it always
works!

**Feedback**
--------

Please send patches or bug reports to <louis.lagendijk@gmail.com>

**Source**
------

You can get a local copy of the development repository with::

    git clone git://github.com/llagendijk/iskra-me162.git


**License**
-------

Copyright (C) 2016 Louis Lagendijk <louis.lagendijk@gmail.com>
Based on previous work by J. Jeurissen and J. van der Linde ((c) 2012/2013)


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
