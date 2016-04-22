import serial
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 10])
plt.ion()

log_file = "live_plot.log"
xbee = "/path/to/xbee/port"

lf = open(log_file, 'a')
ser = serial.Serial(xbee, 19200)

while True:
	try:
		data = ser.readline()
		lf.write(data)
			
		#evaluate to dict like in data version
		dict['agl'] = 0

		y = dict['agl'] 
		plt.scatter(i, y)
		plt.pause(0.05)
	except:
		lf.write("read or plot issue\n")
