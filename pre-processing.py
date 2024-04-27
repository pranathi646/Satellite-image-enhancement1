 #image preprocessing
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# have to convert grayscale back to RGB for plt.imshow(), since
plt.imshow expects a 3d array
# try plotting the same directly with gray_img and see the result for
yourself
plt.imshow(cv2.cvtColor(gray_img, cv2.COLOR_GRAY2RGB))
