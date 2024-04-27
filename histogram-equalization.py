#histogram equalisation
import cv2
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('cyclonee.jpg', cv2.IMREAD_GRAYSCALE)
# Check if the image is loaded successfully
if image is None:
 print("Error: Could not read the image")
 exit()
# Perform histogram equalization
equalized_image = cv2.equalizeHist(image)
# Display the original and equalized images side by side
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.show()
