import pyscreenshot as ImageGrab
import datetime
import time
import sys, select, os
import random

#-----------config--------------

if __name__ == '__main__':
#	freeze_support()

	freq = 10 #min
	image_every = freq * 60 
	path_of_storage = ""

	#-------------------------------

	print "start capturing every " + str(image_every) + " seconds"
	print "Press CTRL^C to stop"
	#last_file = 0
	datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
	while(True):
		try:
			#last_file = str(datetime.datetime.now()).replace(" ","_")
			#file_name = "screenshot_" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + ".png"
			file_name = 'screenshot_%s.png'%datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S')
			print " file name: " + file_name
			ImageGrab.grab_to_file(file_name)
			print "Got another screen capture , " + file_name
			mnt = 60 * random.randint(1,10)
			print mnt
			time.sleep(mnt)		
		except(KeyboardInterrupt, SystemExit):
			sys.exit(0)
