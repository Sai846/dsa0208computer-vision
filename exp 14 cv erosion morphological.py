import cv2
import numpy as np
def apply_erosion(image_path, kernel_size):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_image = cv2.erode(original_image, kernel, iterations=1)
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("eroded_image.jpg", eroded_image)
image_path = "C:/Users/bandi/OneDrive/Pictures/Saved Pictures/images.jpg"
kernel_size = 3 
apply_erosion(image_path, kernel_size)
