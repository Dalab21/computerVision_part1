# Detecting human faces

import cv2.data
import matplotlib.pyplot as plt
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img_path = "img/f1.jpg"
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the images
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 5)

# Draw rectangles arround detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)

# Convert BGR img to RGB for matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the img with rectangles arround detected faces using matplotlib
plt.imshow(img_rgb)
plt.axis('off') #turn off axis level
plt.title('Faces Detection')
plt.show()