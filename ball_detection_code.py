# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 02:57:14 2017

@author: ahmad

Detecting motion and storing the data to a file
"""


import cv2                                   
import numpy as np                           
import imutils


kernel = np.ones((5,5),np.uint8) 

cap = cv2.VideoCapture("test_01.mp4") 


cv2.namedWindow('tracking')



smn = 140    
smx = 255

ti = []
total= 0
fram= 0

with open("Final_Readings.csv","w") as fout:

    xi = []
    yi = []
    ra = []
    while(1):

        buzz = 0
        _, frame = cap.read()
        fram= fram + 1
        print("Frame No:",fram)
        
        if frame is None:
            break
        
        frame = imutils.resize(frame, width=600, height=400)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV,1)
        hue,sat,val = cv2.split(hsv)

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
                   

                 
                    x = float(circles[0][0][0])
                    y = float(circles[0][0][1])
                    r = float(circles[0][0][2])
                    ya = 400 - y
                    xa = 600 - x
                    
                    
                    total = total + 1
                   
                    ti.append(fram)
                    
                    fout.write("{},{},{},{}\n".format(600-x, 400-y, fram, r))
                    print('Detection no', total, 'at',(float(circles[0][0][0]), float(circles[0][0][1])) )
                    
                    xi.append(xa)
                    yi.append(ya)
                    ra.append(r)
                    
                    

        cv2.imshow('tracking',frame)
        
        k = cv2.waitKey(1) & 0xFF
        
r = r*0.212 #converting pixel value to cm

print('Total detections:', total)
print('Detected Object: Ball \nRadius:',"%.2f" % r, 'cms')

cap.release()

cv2.destroyAllWindows()

