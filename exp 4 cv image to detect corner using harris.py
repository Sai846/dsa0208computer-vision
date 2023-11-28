import cv2
import numpy as np
image_path = "C:\Users\bandi\OneDrive\Pictures\Saved Pictures\images.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
threshold = 0.01 * dst.max()
corner_img = np.zeros_like(img)
corner_img[dst > threshold] = [0, 0, 255]  
cv2.imshow('Original Image', img)
cv2.imshow('Corners Detected', corner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
