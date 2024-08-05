import cv2
import numpy as np
i = cv2.imread(r"C:\Users\MEHWISH\OneDrive\Desktop\Rose.jpg")
h , w, _ = i.shape
ul = i[0:h//2, 0:w//2]
ur = i[0:h//2, w//2:w]
dl = i[h//2:h, 0:w//2]
dr = i[h//2:h, w//2:w]
canvas = np.zeros((h, w, 3), dtype=np.uint8)
canvas[0:h//2, 0:w//2]=ul
canvas[0:h//2, w//2:w]=ur
canvas[h//2:h, 0:w//2]=dl
canvas[h//2:h, w//2:w]=dr
cv2.imshow("original image", i)
cv2.imshow("Image Quadrants", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()