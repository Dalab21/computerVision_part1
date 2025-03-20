# Removing noise from image (using Algo OpenCv)

import cv2

#Load noisy img 
noisy_img = cv2.imread('bruit.png')

#Perform img denoising
denoised_img = cv2.fastNlMeansDenoisingColored(noisy_img, None, 10, 10, 7, 21)

#Display
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Denoised Image', denoised_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save
cv2.imwrite('denoised_img.jpg', denoised_img)
