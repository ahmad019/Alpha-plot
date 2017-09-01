
#for using file data

def extract_data(filename):
    labels = []
    fvecs = []
    
    for line in file(filename):
            row = line.split(',')
            labels.append(int(row[0]))
            fvecs.append([float(x)] for x in row[1:2])
        
    fvecs_np = np.matrix(fvecs).astype(np.float32)
    
    labels_np = np.array(labels).astype(dtype=np.uint8)
    
    #labels_onehot = (np.arange(NUM_LABELS) == labels_np[:,None]).astype(np.float32)
    
    return fvecs_np, labels_np
    
    

                       
import matplotlib.pyplot as plt
import numpy as np


xi = []
yi = []
ti = []
labels = []
fvecs = []

with open("Final_Readings.txt","r") as fout:


    for line in fout:
            x, y, t = (item.strip() for item in line.split(',')) 
            
            xi.append(x)
            yi.append(y)
            ti.append(t)
            

extract_data("Final_Readings.txt")



#float(yi.strip().strip("'"))

plt.scatter(ti,yi, c='r') #label='Ball', linewidth=1)  #uncomment to plot 
#plt.plot(ti,xi, 'g', label='Ball', linewidth=1)  #  straight graph

#plt.scatter(xi, yi, c='b')
#plt.plot(xi,yi, 'r')


plt.title('Ball motion')
plt.xlabel('Time --->')
plt.ylabel('Object-Position --->')


plt.show()



    

    


