# Blur Gaussian Effect using OpenCv
import cv2 
import os


img_path = "../data/img1.jpg"

#if not os.path.exists(image_path):
#    print(f"Erreur : L'image '{image_path}' n'existe pas !")
#else:
#    print("L'image existe bien.")


image = cv2.imread(img_path)

blurred_img = cv2.GaussianBlur(image, (15, 15), 0) #(15, 15) is a kernel 

#Display image original and blurred img
cv2.imshow('original image ', image)
cv2.imshow('Blurred image ', blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()