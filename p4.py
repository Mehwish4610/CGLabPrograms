import cv2
import numpy as np
cw=800
ch=600
canvas = np.ones((cw, ch, 3), dtype=np.uint8)*255
objpoints = np.array([[100,100],[200,100],[200,200],[100,200]],dtype=np.int32)
tm = np.float32([[1,0,100],[0,1,50]])
rm = cv2.getRotationMatrix2D((150,150), 45,1)
sm = np.float32([[1.5,0,0],[0,1.5,0]])
to = np.array([np.dot(tm, [x,y,1])[:2] for x,y in objpoints], dtype= np.int32)
ro = np.array([np.dot(rm, [x,y,1])[:2] for x,y in to], dtype= np.int32)
so = np.array([np.dot(sm, [x,y,1])[:2] for x,y in ro], dtype= np.int32)
cv2.polylines(canvas,[objpoints],True,(0,0,0),2)
cv2.polylines(canvas,[to],True,(0,255,0),2)
cv2.polylines(canvas,[ro],True,(255,0,0),2)
cv2.polylines(canvas,[so],True,(0,0,255),2)
cv2.imshow("2d transformation", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()