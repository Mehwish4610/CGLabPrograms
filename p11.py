import cv2
import numpy as np
i = cv2.imread(r"C:\Users\MEHWISH\OneDrive\Desktop\mrbean.png")
gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray , 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ci= i.copy()
cv2.drawContours(ci, contours, -1, (0.255,0), 2)
cv2.imshow("oi",i)
cv2.imshow("contours", ci)
cv2.waitKey(0)
cv2.destroyAllWindows()