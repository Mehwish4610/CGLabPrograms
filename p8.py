import cv2
import numpy as np
i = cv2.imread(r"C:\Users\MEHWISH\OneDrive\Desktop\rose1.png")
h, w, _= i.shape
rm = cv2.getRotationMatrix2D((w/2,h/2), 45, 1)
sm = np.float32([[1.5,0,0],[0,1.5,0]])
tm = np.float32([[1,100,0],[0,1,50]])
ri = cv2.warpAffine(i,rm,(w,h))
si = cv2.warpAffine(i, sm, (int(w*1.5), int(h*1.5)))
ti = cv2.warpAffine(i, tm , (w,h))
cv2.imshow("oi",i)
cv2.imshow("ri",ri)
cv2.imshow("si",si)
cv2.imshow("ti",ti)
cv2.waitKey(0)
cv2.destroyAllWindows()