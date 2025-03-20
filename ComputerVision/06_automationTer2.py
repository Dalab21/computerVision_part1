import cv2
import numpy as np

image_path = "../data/img2.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error : Impossible to load image. Path problem")
    exit()

# gaussian effect
blurred_img = cv2.GaussianBlur(image, (15, 15), 0)

# 2 images in same canal 
if len(image.shape) == 2:  # Images in NG 
    blurred_img = cv2.cvtColor(blurred_img, cv2.COLOR_GRAY2BGR)

# 2 images concatenate horizontaly 
combined = np.hstack((image, blurred_img))

# Display
cv2.imshow("Original & Blurred Images", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
