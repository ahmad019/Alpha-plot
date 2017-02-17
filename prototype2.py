import cv2
import cv2.cv as cv
import numpy as np
import matplotlib.pyplot as plt


kernel = np.ones((5,5),np.uint8)

cap = cv2.VideoCapture("Mobile 720.mp4")



cv2.namedWindow('tracking')



smn = 150
smx = 255

ti = [] #defined list
total= 0

with open("prototype2.txt","w") as fout:

    li = []
    si = []
    while(1):

        buzz = 0
        _, frame = cap.read()
        print("Frame")
        total = total + 1
        print total
        try:
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV,1)
            hue,sat,val = cv2.split(hsv)
        except Exception:
            print("Exception caught")
            break
        

        sthresh = cv2.inRange(np.array(sat),np.array(smn),np.array(smx))


        tracking = sthresh
	
	ti.append(total) #Append with each value of the frame
        

        dilation = cv2.dilate(tracking,kernel,iterations = 1)
        closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
        closing = cv2.GaussianBlur(closing,(5,5),0)

        circles = cv2.HoughCircles(closing,cv.CV_HOUGH_GRADIENT,2,120,param1=120,param2=50,minRadius=10,maxRadius=0)


        if circles is not None:
                for i in circles[0,:]:
                  
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,0,255),5)
                    cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),2,(0,0,255),10)
                  
                    buzz = 1
                   

                    fout.write((str(circles[0][0][0])) + ", " + str(circles[0][0][1]) + "\n" )
                    print (str(circles[0][0][0])) +", "+ str(circles[0][0][1])
                    x = str(circles[0][0][0])
                    y = str(circles[0][0][1])
                    li.append(x)
                    si.append(y)

        cv2.imshow('tracking',frame)
        
        k = cv2.waitKey(50) & 0xFF
        if k == 27:
            break

print(ti) #print to check
print(li)
print(si)
plt.scatter(si,ti, label='Ball', color='k', s=23, marker='o') #plot x vs ti 
plt.scatter(li,ti, label='Ball', color='k', s=23, marker='o') #plot y vs ti
plt.show()
		    

cap.release()

cv2.destroyAllWindows()

