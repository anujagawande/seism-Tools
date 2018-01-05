import math
import numpy as np
from scipy.integrate import cumtrapz
from time import gmtime, strftime
import os.path

#calculating S(x1,x2)
def spg(c1, c2):
	num = (c1-c2)
	denom = min(c1,c2)
	z2 = (num/denom)**2
	return 10*(math.exp(-z2))

#-------------------------------------------------------------------
def A(series1, series2):#taking 2 accelertaion time series as parameters
	#getting absolute values of both series
	absv = np.absolute(series1)
	absv2 = np.absolute(series2)
	#getting max
	p1 = np.amax(absv) 
	p2 = np.amax(absv2)
	return p1,p2

#-------------------------------------------------------
def peak_acceleration(A1, A2):

	value = A(A1,A2)
	return spg(value[0],value[1])

#-------------------------------------------------------
def peak_velocity(V1, V2):
	value = A(V1,V2)
	return spg(value[0],value[1])

#-------------------------------------------------------
def peak_displacement(D1, D2):
	value = A(D1,D2)
	return spg(value[0],value[1])	

#--------------------------------------------------------
#calculating arias integral
def arias_integral(t,acc):
	G = 9.80665
	y = np.square(acc)
	ai = cumtrapz(y, x=t, initial = 0)
	ai = (math.pi/(2*G)) * ai
	return ai

#-------------------------------------------------------------------
def energy_integral(t,vel):
	y = np.square(vel)
	ei = cumtrapz(y, x=t, initial=0)
	return ei

#---------------------------------------------------------------------
def arias_energy_duration(data, data2):
	final_integral = len(data)-1
	N1_final = np.array([])
	for x in range(0,len(data)):
		N1 = data[x]/data[final_integral]
		N1_final = np.append(N1_final,[N1])

	final_integral2 = len(data2)-1
	N2_final = np.array([])
	for x in range(0,len(data2)):
		N2= data2[x]/data2[final_integral2]
		N2_final = np.append(N2_final,[N2])

	F = abs(N1_final-N2_final)
	c = 10*(1-max(F))
	return c
#------------------------testing-------------------------------
#acc1 = (1.1,2.2,3.3)
#acc2 = (6.2,5.7,4.2)
#t = 0,1,2
#print (arias_energy_duration(acc1,acc2))


#-------------------------------Main-----------------------------------	

if __name__ == "__main__":

	time = [np.array([],float)]
	dis = [np.array([],float)]
	vel = [np.array([],float)]
	acc = [np.array([],float)]
	time2 = [np.array([],float)]
	dis2 = [np.array([],float)]
	vel2 = [np.array([],float)]
	acc2 = [np.array([],float)]

	#reading data from file
	try:
		time, dis, vel, acc = np.loadtxt('testdata.txt',skiprows=1,unpack = True);
		time2, dis2, vel2, acc2 = np.loadtxt('testdata2.txt',skiprows=1,unpack = True);
	except IOError:
		print("Error loading file.")
		sys.exit(1)

	#print (dis)

	#getting scores
	#c1
	data = arias_integral(time,acc)
	data2 = arias_integral(time2,acc2)
	c1 = arias_energy_duration(data,data2)

	#c2
	data3 = energy_integral(time,vel)
	data4 = energy_integral(time2,vel)
	c2 = arias_energy_duration(data3, data4)

	#c3
	#data5 = arias_intensity(time[time.size-1],acc[acc.size-1])
	#data6 = arias_intensity(time2[time2.size-1],acc2[acc2.size-1])
	c3 = spg(data[len(data)-1], data2[len(data2)-1])

	#c4
	#data7 = energy_integral(time[time.size-1],vel[vel.size-1])
	#data8 = energy_integral(time2[time2.size-1],vel2[vel2.size-1])
	c4 = spg(data3[len(data3)-1], data4[len(data4)-1])

	#c5, c6, c7
	c5 = peak_acceleration(acc, acc2)
	c6 = peak_velocity(vel, vel2)
	c7 = peak_displacement(dis, dis2)

	x = np.array([c1,c2,c3,c4,c5,c6,c7])
	x1 = np.round([c1, c2,c3,c4,c5,c6,c7 ],2)
	x1 = x.tolist()
	#print x1
	#print x

	#saving scores to scores folder in testing
	actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

	save_path = '/Users/anuja/Desktop/testing/scores'
	fileName = os.path.join(save_path, 'scores' + str(actual_time)+".txt")   

	np.savetxt(fileName, x1 , delimiter=' ',header="c1 c2 c3 c4 c5 c6 c7",comments="", fmt='%f')


'''
#randomData = ("Some Random stuff")
t,s = str(time.time()).split('.')
filename = "test_" +t+".txt"
#print ("writing to", filename)
with open(filename, "w") as current:
    current.write(x)
'''
	
