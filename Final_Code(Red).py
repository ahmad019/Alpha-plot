# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:57:14 2017

@author: ahmad
"""


import cv2                                   
import numpy as np                           
import matplotlib.pyplot as plt
import imutils


kernel = np.ones((5,5),np.uint8) 

cap = cv2.VideoCapture("test_01.mp4") 


cv2.namedWindow('tracking')



smn = 140    
smx = 255

ti = []
total= 0
fram= 0

with open("Final_Readings.txt","w") as fout:

    xi = []
    yi = []
    while(1):

        buzz = 0
        _, frame = cap.read()
        fram= fram + 1
        print("Frame No:",fram)
        
#        if frame is None:
 #           break

  	
        try:
            frame = imutils.resize(frame, width=600, height=400)
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV,1)
            hue,sat,val = cv2.split(hsv)
        except Exception:
            print("Exception caught")
            break
        

        sthresh = cv2.inRange(np.array(sat),np.array(smn),np.array(smx))


        tracking = sthresh

       

        
        

        dilation = cv2.dilate(tracking,kernel,iterations = 1)
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
        closing = cv2.GaussianBlur(closing,(5,5),0)

        circles = cv2.HoughCircles(closing,cv2.HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)


        if circles is not None:
                for i in circles[0,:]:
                  
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,0,255),5)
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,0,255),10)
                  
                    buzz = 1
                   

#                    fout.write((str(circles[0][0][0])) + ", " + str(circles[0][0][1]) + "\n" )
                    #print (str(circles[0][0][0]).format(circles[0][0][1]))
                    x = float(circles[0][0][0])
                    y = float(circles[0][0][1])
                    ya = 400 - y
                    
                    
                    total = total + 1
                    #ti.append(total*2)
                    ti.append(fram)
                    
                    fout.write("{},{},{}\n".format(x, 400-y, fram))
                    print('Detection no', total, 'at',(float(circles[0][0][0]), float(circles[0][0][1])) )
                    
                    xi.append(x)
                    yi.append(ya)
                    
                    

        cv2.imshow('tracking',frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

print('total detections', total)



#print(xi)
print(yi)

#plt.plot(ti,yi, 'r', label='Ball', linewidth=1)  #uncomment to plot 
#plt.plot(ti,xi, 'g', label='Ball', linewidth=1)  #  straight graph

#plt.scatter(ti, xi, c='r')  #scatter plot
plt.scatter(ti, yi, c='b')  # of x and y

#plt.scatter(xi, yi, c='r')
#plt.plot(yi,xi, 'r')


plt.title('Ball motion')
plt.xlabel('Time --->')
plt.ylabel('Object-Position --->')


plt.show()
		    

cap.release()

cv2.destroyAllWindows()

