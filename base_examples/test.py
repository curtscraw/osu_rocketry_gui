import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 10])
plt.ion()

for i in range(100):
	y = i 
	plt.scatter(i, y)
	plt.pause(0.05)

while True:
	plt.pause(0.05)
