#constrast strecthing
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_path = 'cyclonee.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Check if the image is loaded successfully
if original_image is None:
 print("Error: Could not read the image")
 exit()
# Define the parameters for high-contrast stretching
alpha = 1.5 # Adjust this parameter for different levels of contrast
# Apply high-contrast stretching
stretched_image = cv2.convertScaleAbs(original_image, alpha=alpha)
# Display the original and high-contrast stretched images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_image, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Contrast Stretched Image')
plt.imshow(stretched_image, cmap='gray')
plt.axis('off')
plt.show()
