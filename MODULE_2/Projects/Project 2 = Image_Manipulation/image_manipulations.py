import cv2
import matplotlib.pyplot as plt

image = cv2.imread("MODULE_2\Assets\Images\ex_img_L8.jpg")

img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cropping the image
cropped_rgb = img_rgb[100:300, 200:400]


# Rotating the image
(h,w) = image.shape[:2]

center = w//2, h//2
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_rgb = cv2.warpAffine(img_rgb, M, (w, h))



# FIGURES
plt.figure(1)
plt.imshow(img_gray, cmap = 'gray')
plt.title("Grayscale Image")

plt.figure(2)
plt.imshow(cropped_rgb)
plt.title("Cropped RGB Image")

plt.figure(3)
plt.imshow(rotated_rgb)
plt.title("Rotated RGB Image")



plt.show()