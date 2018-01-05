import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.mlab as mlab
import pylab as pl
import collections
import math
import timeit
from time import gmtime, strftime
import os.path
import glob
import os
import sys

def fft(a,n):
	freq = np.array([])
	freq = np.fft.fft(a,n)
	return freq

if __name__ == "__main__":
	
	n = int(sys.argv[1])
	#n2 = int(sys.argv[2])
	#n3 = int(sys.argv[3])
	input_path = sys.argv[2]
	graph_path = sys.argv[3]
	
	#print input_path
	#print graph_path

	
	#reading a time signal from file
	path = input_path + '/*'
	list_of_files = glob.glob(path) 
	recent_data = sorted(list_of_files, key=os.path.getmtime)
	a = [np.array([],float)]
	try:
		time,dis,vel,a = np.loadtxt(recent_data[-1] ,skiprows=1,unpack = True);
	except IOError:
		print("Error loading file.")
		sys.exit()


	'''
	#reading second time signal
	a2 = [np.array([],float)]
	try:
		time2,a2 = np.loadtxt(recent_data[-2] ,skiprows=1,unpack = True);
	except IOError:
		print("Error loading file.")
		sys.exit()

	#reading third time signal
	a3 = [np.array([],float)]
	try:
		time3,a3 = np.loadtxt(recent_data[-3] ,skiprows=1,unpack = True);
	except IOError:
		print("Error loading file.")
		sys.exit()
	'''

	#n = 256
	#if n is size of a, N is next power of 2
	if n == len(a):
		if n == 0.0 or n == 1.0:
			n = 2.0
		else:
			n = int(2**(math.ceil(math.log(n, 2))))
	#print n		
	A = np.array([])
	A = fft(a,n)
	A = A[range(int(len(A)/2))]
	#print A

	'''
	#print A
	n2 = 10
	#if n is size of a, N is next power of 2
	
	if n2 == len(a):
		if n2 == 0.0 or n2 == 1.0:
			n2 = 2.0
		else:
			n2 = int(2**(math.ceil(math.log(n2, 2))))
	'''

	#print n		
	velocity = np.array([])
	velocity = fft(vel,n)
	velocity = velocity[range(int(len(velocity)/2))]
	#print A2

	'''
	n3 = 25
	#if n is size of a, N is next power of 2
	if n3 == len(a):
		if n3 == 0.0 or n3 == 1.0:
			n3 = 2.0
		else:
			n3 = int(2**(math.ceil(math.log(n3, 2))))
	#print n	
	'''	
	displ = np.array([])
	displ = fft(dis,n)
	displ = displ[range(int(len(displ)/2))]

	#print A3
	
	#------------------------------------------------------------------------------------------------
	#plotting time and amplitude fourier spectrum(frequency) 
	#fs = 100 # Or whatever the actual sample rate is (Hz)
	#Number of samples/sample 
	#fs = 21
	
	fig = plt.figure()	
	gs = gridspec.GridSpec(3, 3)

	ax1 = fig.add_subplot(gs[0,:-1])
	ax1.plot(time,a,'green')
	plt.title ('Time signal')
	plt.xlabel('Acc')
	plt.ylabel('Time')
	

	deltat = time[1]-time[0]
	nyquist = 1/(2*deltat)


	deltat_f = nyquist/(n/2)
	i = 1
	f = np.array([])
	value = 0
	while value<nyquist:	
		value = i * deltat_f
		f = np.append(f,[value])
		i += 1

	#print deltat,nyquist,deltat_f ,f 
	
	#f = np.linspace(0,nyquist,num = nyquist, endpoint=True)#check endpoint settting...

	abs_A = np.absolute(A)
	amp = abs_A[0:len(f)]
	ax2 = fig.add_subplot(gs[0,2])
	ax2.plot(f,amp, 'r-')
	plt.title ('AFS')
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Amplitude')

	
	ax3 = fig.add_subplot(gs[1,:-1])
	ax3.plot(time,vel,'green')
	plt.title ('Time signal')
	plt.xlabel('Vel')
	plt.ylabel('Time')
	
	'''
	deltat2 = time2[1]-time2[0]
	nyquist2 = 1/(2*deltat2)

	deltat_f2 = nyquist2/(n2/2)
	j = 1
	f2 = np.array([])
	value2 = 0
	while value2<nyquist2:	
		value2 = j * deltat_f2
		f2 = np.append(f2,[value2])
		j += 1
	'''



	#f2 = np.linspace(0,nyquist2,num = nyquist2, endpoint=True)#check endpoint settting...

	abs_A2 = np.absolute(velocity)	
	amp2 = abs_A2[0:len(f)]
	ax4 = fig.add_subplot(gs[1,2])
	ax4.plot(f, amp2, 'r-')
	plt.title ('AFS')
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Amplitude')

	ax5 = fig.add_subplot(gs[2,:-1])
	ax5.plot(time,dis,'green')
	plt.title ('Time signal')
	plt.xlabel('Dis')
	plt.ylabel('Time')
	
	'''
	deltat3 = time3[1]-time3[0]
	nyquist3 = 1/(2*deltat3)

	deltat_f3 = nyquist3/(n3/2)
	k = 1
	f3 = np.array([])
	value3 = 0
	while value3<nyquist3:	
		value3 = k * deltat_f3
		f3 = np.append(f3,[value3])
		k += 1
	'''

	#f3 = np.linspace(0,nyquist3,num = nyquist3, endpoint=True)#check endpoint settting...

	
	abs_A3 = np.absolute(displ)
	amp3 = abs_A3[0:len(f)]
	ax6 = fig.add_subplot(gs[2,2])
	ax6.plot(f,amp3 , 'r-')
	plt.title ('AFS')
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Amplitude')
	
	#gs.update(wspace=0.5, hspace=0.5)
	plt.tight_layout()
	fig = plt.gcf()

	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())
	save_path = graph_path
	#save_path = '/Users/anuja/Desktop/testing/fft/plots'
	file_name = os.path.join(save_path, 'time_aft_plot' + str(actual_time)+".png")
	plt.savefig(file_name)
	plt.show()
	# to produce time and frequency graphs side by side
	#plt.subplot(1, 2, 1)
	#plt.subplot(1, 2, 2)
	#plt.tight_layout()
	#signal2
	



	#f = 21
	
	#for i in range(0,(n/2)+1):
	#	f = (Fs*i)/n;
	#P = abs(A/n);

	#plt.plot(f,P[1:n/2+1]) 
	#title('Amplitude fourier Transform')
	#xlabel('Frequency (f)')
	#ylabel('|P(f)|')
	

	