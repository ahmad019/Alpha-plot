
#for finding the velocity and acceleration of motion

                       
import matplotlib.pyplot as plt
import numpy as np
import math

def finddisplacement(x,y): #defining function to find euclidean displacement
    arr = []
    for i in range(np.shape(x)[0]-1):
        d = math.sqrt( ((x[i+1]-x[i])*(x[i+1]-x[i]))+((y[i+1]-y[i])*(y[i+1]-y[i])) ) 
        arr.append(d)
    return arr
def findvelocity(d,t):  #function for finding velocity 
    v = []    
    for i in range(np.shape(d)[0]):
        ve = d[i]/t[i]
        v.append(ve)
    return v

def findacceleration(v,t):  #function for finding acceleration
    a = []
    for i in range(np.shape(v)[0]-1):
        ai = (v[i+1]-v[i])/t[i]
        a.append(ai)
    return a
        


xi = []
yi = []
ti = []
xt = []


with open("Final_Readings.txt","r") as fout:


    for line in fout:
            x, y, t = (item.strip() for item in line.split(',')) 
            
            xi.append(float(x))
            yi.append(float(y))
            ti.append(float(t))
            


dist = finddisplacement(yi,ti) 
vel = findvelocity(dist,ti)
accel = findacceleration(vel,ti)
print(ti)
#plt.plot( ti[0:45],dist)
#plt.plot(ti[0:45], vel)
plt.plot(ti[0:44], accel)
plt.show()
#for i in range(np.shape(x)[0]-1):
 #   xd = math.sqrt()
#float(yi.strip().strip("'"))

plt.scatter(ti,yi, c='r') #label='Ball', linewidth=1)  #uncomment to plot 
#plt.plot(ti,xi, 'g', label='Ball', linewidth=1)  #  straight graph

#plt.scatter(xi, yi, c='b')
#plt.plot(xi,yi, 'r')


plt.title('Ball motion')
plt.xlabel('Time --->')
plt.ylabel('Object-Position --->')


plt.show()