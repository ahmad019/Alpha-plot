
#for using file data

                       
import matplotlib.pyplot as plt


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
            




plt.title('Ball motion')
plt.xlabel('Time --->')
plt.ylabel('Object-Position --->')

plt.scatter(ti,yi, c='r') #label='Ball', linewidth=1)  #uncomment to plot
plt.show() 
plt.plot(ti,xi, 'g', label='Ball', linewidth=1)  #  straight graph
plt.show()

#plt.scatter(xi, yi, c='b')
#plt.plot(xi,yi, 'r')

