#image acquisition
from google.colab import files
uploaded = files.upload()
!pip install opencv-python
import cv2
import numpy as np
import matplotlib.pyplot as plt
# read an image
img = cv2.imread('cyclonee.jpg')
# Let's see how the image looks like
plt.imshow(img)
