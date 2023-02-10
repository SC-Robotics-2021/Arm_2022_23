import time
from roboclaw_3 import Roboclaw

#Windows comport name
# rc = Roboclaw("COM7",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()

#Get version string
for x in range(0,255):
	value = rc.WriteEeprom(0x80,x,x*2)
	print ("EEPROM:"),
	print (x),
	print (" "),
	if value==False:
		print ("Failed")
	else:
		print ("Written")
