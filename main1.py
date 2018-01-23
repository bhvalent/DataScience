#AmethystImpala
#8/28/17
#Challenge 1
#http://www.pythonforbeginners.com/
#https://stackoverflow.com/questions/42758897/change-line-width-of-lines-in-matplotlib-pyplot-legend
#Lecture notes and powerpoint

from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot


#Manipulating the data
data = open("AmethystImpala_ch1.csv", "r")
data = data.read()
data = data.replace(" ", "")
data = data.split("\n")
data.pop()

for x in range(len(data)):
	data[x] = data[x].split(",")
	data[x][0] = np.float64(data[x][0])
	data[x][1] = np.float64(data[x][1])
	data[x][2] = np.float64(data[x][2])



#separating data by tower
tower1 = []
tower2 = []

for x in data:
	if x[2] > 50:
		tower1.append(x)
	else:
		tower2.append(x)


#Separating data in each line by axis for graphing
x1ax = []
y1ax = []
for line in tower1:
	x1ax.append(line[0])
	y1ax.append(line[1])

x2ax = []
y2ax = []
for line in tower2:
	x2ax.append(line[0])
	y2ax.append(line[1])



#Finding the average amplitude for each time
average = []
milliAxes = []
milli = 0
while milli <= tower2[len(tower2) - 1][0]:
	total = 0
	count = 0
	for line in tower2:
		if line[0] == milli:
			total += line[1]
			count += 1
	if count > 0:
		average.append(total/count)
		milliAxes.append(milli)
	milli += 1



#Plotting data on graph
mplot.title("Challenge 1")
mplot.xlabel("Milliseconds")
mplot.ylabel("Amplitude")

mplot.scatter(x2ax, y2ax, color = "red", marker = "o")
mplot.plot(milliAxes, average, color = "blue", linestyle = "-", linewidth = 4.0)
mplot.show()


