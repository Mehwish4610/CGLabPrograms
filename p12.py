import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
i = cv2.imread(r"C:\Users\MEHWISH\OneDrive\Desktop\mrbean.png")
gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=5, minSize=(30,30))
for (x,y,w,h) in faces:
    cv2.rectangle(i, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("face detection", i)
cv2.waitKey(0)
cv2.destroyAllWindows()