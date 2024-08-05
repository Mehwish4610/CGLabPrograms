import cv2
import numpy as np
i = cv2.imread(r"C:\Users\MEHWISH\OneDrive\Desktop\rose1.png")
gray= cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
kernel = np.ones((5,5), np.float32)/25
texture = cv2.filter2D(gray, -1, kernel)
cv2.imshow("oi",i)
cv2.imshow("edges", edges)
cv2.imshow("textures", texture)
cv2.waitKey(0)
cv2.destroyAllWindows()