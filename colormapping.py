import cv2
import matplotlib.pyplot as plt
# Load the cyclone image
image_path = 'cyclonee.jpg'
cyclone_image = cv2.imread(image_path)
# Check if the image is loaded successfully
if cyclone_image is None:
 print("Error: Could not read the image")
 exit()
# Convert the image to grayscale
gray_image = cv2.cvtColor(cyclone_image, cv2.COLOR_BGR2GRAY)
# Apply a color map for visualization (you can choose a different
colormap)
color_mapped_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)
# Display the original and color-mapped images
plt.subplot(1, 2, 1)
plt.title('Original Cyclone Image')
plt.imshow(cv2.cvtColor(cyclone_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Color-Mapped Image')
plt.imshow(cv2.cvtColor(color_mapped_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
