import cv2 as cv
import numpy as np
 # pylint: disable=no-member


 
def edge_demo(image):
    cannyThreshold = 180
    maxLinesNum = 12
    min_line_length = 20
    max_line_gap = 200
    mid = cv.Canny(image,cannyThreshold,450)
    mid = cv.threshold(mid,128,255,cv.THRESH_BINARY)
    edgeDetect = cv.cvtColor(mid,cv.COLOR_GRAY2RGB)
    lines = cv.HoughLinesP(mid, 1,np.pi/180,80,min_line_length,max_line_gap)
    while(lines.size() >= maxLinesNum):
        cannyThreshold += 2
        mid = cv.Canny(image,cannyThreshold,cannyThreshold*2.5)
        mid = cv.threshold(mid,128,255,cv.THRESH_BINARY)
        edgeDetect = cv.cvtColor(mid,edgeDetect,cv.COLOR_GRAY2RGB)
        lines = cv.HoughLinesP(mid,1,np.pi/180,80,min_line_length,max_line_gap)
        edge_output = mid
    cv.imshow("Canny edge",edge_output)
    
src = cv.imread('./source/unprocessed_picture.jpeg')

cv.namedWindow('input_picture',cv.WINDOW_NORMAL)
cv.imshow('input_picture',src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
