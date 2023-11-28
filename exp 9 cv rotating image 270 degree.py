import cv2
import numpy as np
image_path = "C:/Users/bandi/OneDrive/Pictures/Saved Pictures/images.jpg"
original_img = cv2.imread(image_path)
height, width = original_img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 270, 1)
rotated_img = cv2.warpAffine(original_img, rotation_matrix, (width, height))
cv2.imshow('Original Image', original_img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
