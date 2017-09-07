
"""
For using file data to plot different graphs of the motion

"""
              
import matplotlib.pyplot as plt
import numpy as np

xi = []
yi = []
ti = []


with open("Final_Readings.csv","r") as fout:


    for line in fout:
            x, y, t, r = (item.strip() for item in line.split(',')) 
            
            xi.append(float(x))
            yi.append(float(y))
            ti.append(float(t))
            



plt.scatter(ti,yi, c='r')
plt.title('Vertical displacement vs Time')
plt.show() 

plt.plot(ti,xi, 'g', label='Ball', linewidth=1)  #  straight graph
plt.title('Horizontal displacement vs Time')
plt.show()

ti = np.array(ti)   #converting into
yi = np.array(yi)       # numpy array

z = np.polyfit(ti,yi,2)   #data fitting

f = np.poly1d(z)     #initializing a polynomial

x_new = np.linspace(ti[0], ti[-1], 50) #plotting the ploynomial deg 2
y_new = f(x_new)

plt.plot(ti,yi,'o', x_new, y_new) #to plot the best fit curve
plt.title('Best fit curve')
plt.show()

plt.title('Original Motion')
plt.plot(x_new,y_new, 'y')

