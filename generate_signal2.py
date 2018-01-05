from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from time import gmtime, strftime
import os.path
import pylab as pl
import os.path
import glob
import os
import sys

#finds value of gaussian function 
def gaussian(x, a, b, c):

	#for storing calculated values in a numpy array
	#data = np.empty((0, 100))
	e = 2.71828
	#for x in range(0,x+1):
	num = -((x-b)**2)
	den = 2.0*(c**2)
	value1 = a*(e**(num/den))
	#data = np.append(data, [value1])
	return value1


#-------------------------------Main-----------------------------------	
if __name__ == "__main__":
	t = int(input('Enter the maximum time of signal:'))
	a = float(input('Enter a:'))
	b = float(input('Enter b:'))
	c = float(input('Enter c:'))
	deltat = float(input('Enter delta t:'))
	'''
	a = 6
	b = 8
	c = 10
	deltat = 0.001
	t = 1
	'''

	N = int(t/deltat)
	#increasing N by 1
	N = N+1
	time2 = np.arange(0,N,deltat)#

	g2 = np.array([])
	for i in range(0,len(time2)):
		value = gaussian(time2[i],a,b,c)
		g2 = np.append(g2, [value])
	#print g2
	
	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/signals_2'
	fileName = os.path.join(save_path, 'signal2' + str(actual_time)+".txt") 
	np.savetxt(fileName, zip(time2,g2), delimiter=' ',header="time      acc      ",comments="", fmt='%f')
	

	#------------------------------------------------------
	f = np.array([])	
	for i in range(0,N):
		value = gaussian(i*deltat,a,b,c)
		f = np.append(f,[value])
	#print f
	
	#plotting----------------------------------------------------------------------------------------------
	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/signals_3'
	fileName = os.path.join(save_path, 'signal3' + str(actual_time)+".txt") 
	np.savetxt(fileName, zip(time2,f), delimiter=' ',header="time        acc      ",comments="", fmt='%f')

	#reading data from two recent files
	list_of_files = glob.glob('/Users/anuja/Desktop/testing/signals_2/*') 
	recent_data = sorted(list_of_files, key=os.path.getmtime)

	#signal 1
	try:
	#reading data from file and ploting
		plt.plotfile(recent_data[-1],('time','acc'), delimiter=' ', marker='None',newfig=True, subplots=True)
	except IOError:
		print("Error reading file.")
		sys.exit(1)

	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/plots_2'
	file_name = os.path.join(save_path, 'signal_2' + str(actual_time)+".png")

	pl.savefig(file_name, bbox_inches='tight')

#-------------------------------------------------------------------------------------------------------------------------
	#reading data from two recent files
	list_of_files = glob.glob('/Users/anuja/Desktop/testing/signals_3/*') 
	recent_data = sorted(list_of_files, key=os.path.getmtime)

	#signal 1
	try:
	#reading data from file and ploting
		plt.plotfile(recent_data[-1],('time','acc'), delimiter=' ', marker='None',newfig=True, subplots=True)
	except IOError:
		print("Error reading file.")
		sys.exit(1)

	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/plots_3'
	file_name = os.path.join(save_path, 'signal_3' + str(actual_time)+".png")

	pl.savefig(file_name, bbox_inches='tight')





