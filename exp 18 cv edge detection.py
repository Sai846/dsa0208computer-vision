import cv2
import numpy as np
image = cv2.imread("C:/Users/bandi/OneDrive/Documents/vision.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Could not open or find the image.")
    exit()
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = np.uint8(np.absolute(sobel_x))
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
