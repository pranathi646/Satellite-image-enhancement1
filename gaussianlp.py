#gaussian lp filtering
img = cv2.imread('cyclonee.jpg')
assert img is not None, "file could not be read, check with
os.path.exists()"
blur = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
