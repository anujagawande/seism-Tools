import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab as pl
from time import gmtime, strftime
import os.path
import glob
import os
import sys


def plot():
	#reading data from two recent files
	list_of_files = glob.glob('/Users/anuja/Desktop/testing/signals/*') 
	recent_data = sorted(list_of_files, key=os.path.getmtime)

	#signal 1
	try:
	#reading data from file and ploting
		plt.plotfile(recent_data[-1],('time','dis','vel','acc'), delimiter=' ', marker='None',newfig=True, subplots=True)
	except IOError:
		print("Error reading file.")
		sys.exit(1)

	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/plots'
	file_name = os.path.join(save_path, 'signal_1' + str(actual_time)+".png")

	pl.savefig(file_name, bbox_inches='tight')
	plt.show()
'''
#-----------------------------------------------------------------------------------------------------------------------
	#signal 2
	try:
		#reading data from file and ploting
		plt.plotfile(recent_data[-2],('Time','Dis','Vel','Acc'), delimiter=' ', marker='None',newfig=True, subplots=True)
	except IOError:
		print("Error reading file.")
		sys.exit(1)

	actual_time2 = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path2 = '/Users/anuja/Desktop/testing/plots'
	file_name2 = os.path.join(save_path2, 'signal_2' + str(actual_time2)+".png")

	pl.savefig(file_name2, bbox_inches='tight')
	plt.show()
'''
#-------------------------------Main-----------------------------------	
if __name__ == "__main__":

	plot()