"""
for finding the velocity and acceleration of motion

and Analyzing data to calculate the value of g

"""

import matplotlib.pyplot as plt
import numpy as np


def findvelocity(d,t):  #function for finding velocity 
    v = []    
    for i in range(len(d)-1):
        ve = (d[i+1]-d[i])/(t[i+1]-t[i])
        v.append(ve)
    return v

def findacceleration(v,t):  #function for finding acceleration
    a = []
    for i in range(len(v)-1):
        ai = (v[i+1]-v[i])/(t[i+1]-t[i])
        a.append(ai)
    return a


xi = []
yi = []
ti = []


with open("Final_Readings.csv","r") as fout:


    for line in fout:
            x, y, t, r = (item.strip() for item in line.split(',')) 
            
            xi.append(float(x))
            yi.append(float(y))
            ti.append(float(t))
            




vel = findvelocity(yi,ti)  #calling fucn to cal. Velocity
accel = findacceleration(vel,ti)    #calling fucn to calculate Acceleration

v = ( (np.mean(vel) * 0.2125 ) * 240)
a = ( (np.mean(accel) * 0.2125) * (240*240))

ti = np.array(ti)   #converting into
yi = np.array(yi)       # numpy array

z = np.polyfit(ti,yi,2)   #data fitting

f = np.poly1d(z)     #initializing a polynomial

x_new = np.linspace(ti[0], ti[-1], 50) #plotting the ploynomial deg 2
y_new = f(x_new)

plt.plot(ti,yi,'o', x_new, y_new) #to plot the best fit curve
plt.title('Best fit curve')
plt.show()


g = ( ((z[0]*2)*0.2125) * (240*240))  #acceleration due to gravity

plt.plot(ti[0:45], vel, c='g')
plt.title('Velocity-Time graph')
plt.show()
plt.plot(ti[0:44], accel, c='b')
plt.title('Acceleration-Time graph')
plt.show()

print('\nAcceleration due to gravity:' ,"%.2f" % g, 'cm/s^2')
print('\nAverage Velocity: ', "%.2f" % v, 'cm/s^2' )
print('\nAverage acceleration:' ,"%.2f" % a, 'cm/s^2')

