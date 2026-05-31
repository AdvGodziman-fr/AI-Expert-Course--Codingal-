import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = "MODULE_2/example_img.jpg"

image = cv2.imread(filename)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h,w) = image.shape[:2]

center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_rgb = cv2.warpAffine(image_rgb, M, (w, h))

plt.figure(1)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")

# Increase brightness by adding 50 to all pixel values
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50

brighter = cv2.add(image, brightness_matrix)
brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)


# Use cv2.add to avoid negative values or overflow

plt.figure(2)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")

plt.show()