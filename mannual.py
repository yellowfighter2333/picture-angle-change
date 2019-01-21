import numpy as np
import cv2
from transform import four_point_transformation
cnt = 0
img = cv2.imread('./source/3.jpeg')
cv2.namedWindow('image')
pts = np.zeros((4,2),dtype = 'float32')
def deter_point(event,x,y,flags,param):
    global cnt    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,255,0),thickness=-1)
        print(x,y)
        if cnt in range(0,4):
                pts[cnt] = (x,y)
                print("the",(cnt + 1),"position point is determined")
        if cnt == 3:
                print(pts)
                warped = four_point_transformation(img,pts)
                cv2.namedWindow('warped')
                cv2.imshow('warped',warped)
        cnt = cnt + 1
cv2.setMouseCallback('image',deter_point)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()