import cv2
import numpy as np
def apply_dlt(image_path, output_size):
    original_image = cv2.imread(image_path)
    source_points = np.float32([[50, 50], [200, 50], [200, 200], [50, 200]])
    destination_points = np.float32([[0, 0], [output_size[0] - 1, 0], [output_size[0] - 1, output_size[1] - 1], [0, output_size[1] - 1]])
    A = []
    for i in range(4):
        x, y = source_points[i]
        u, v = destination_points[i]
        A.append([-x, -y, -1, 0, 0, 0, x * u, y * u, u])
        A.append([0, 0, 0, -x, -y, -1, x * v, y * v, v])
    A = np.array(A)
    _, _, V = np.linalg.svd(A)
    homography_matrix = V[-1, :].reshape((3, 3))
    transformed_image = cv2.warpPerspective(original_image, homography_matrix, output_size)
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("transformed_image_dlt.jpg", transformed_image)
image_path = "C:/Users/bandi/OneDrive/Pictures/Saved Pictures/images.jpg"
output_size = (300, 200)  
apply_dlt(image_path, output_size)
