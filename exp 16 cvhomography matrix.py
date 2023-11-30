import cv2
import numpy as np
def apply_homography(image_path, output_size):
    original_image = cv2.imread(image_path)
    source_points = np.float32([[50, 50], [200, 50], [200, 200], [50, 200]])
    destination_points = np.float32([[0, 0], [output_size[0] - 1, 0], [output_size[0] - 1, output_size[1] - 1], [0, output_size[1] - 1]])
    homography_matrix, _ = cv2.findHomography(source_points, destination_points)
    transformed_image = cv2.warpPerspective(original_image, homography_matrix, output_size)
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("transformed_image.jpg", transformed_image)
image_path ="C:/Users/bandi/OneDrive/Pictures/Saved Pictures/images.jpg"
output_size = (300, 200)  
apply_homography(image_path, output_size)
