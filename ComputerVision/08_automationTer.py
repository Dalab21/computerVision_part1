# Bilateral Filter on Image using openCv
import cv2.data
import matplotlib.pyplot as plt
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img_path = "img/f1.jpg"
img = cv2.imread(img_path)

# Bilateral filter apply
bilateral_filter_image = cv2.bilateralFilter(img, 9, 75, 75)

# Convert BGR to RGB for displaying image
bilateral_filter_img_rgb = cv2.cvtColor(bilateral_filter_image, cv2.COLOR_BGR2RGB)


# Display the img with rectangles arround detected faces using matplotlib
plt.subplot(1, 2, 1)
plt.title('Original image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Bilateral filtered image')
plt.imshow(bilateral_filter_img_rgb)
plt.axis('off') #turn off axis level

plt.tight_layout()
plt.show()