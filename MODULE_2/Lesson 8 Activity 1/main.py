import cv2
import matplotlib.pyplot as plt

# Reads the image into memory
image = cv2.imread("MODULE_2\Assets\Images\ex_img_L8.jpg")

# Convert BGR to RGB
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Display image data as a plot, interpreting values as colors
plt.figure(1)
plt.imshow(img_rgb)
plt.title("RGB Image")

# Convert to Grayscale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(2)
plt.imshow(img_gray, cmap = 'copper')
plt.title("Grayscale Image")

# INTERNAL OPERATION: Compute a single-channel grayscale image -- GrayPixel = 0.299*R + 0.587*G + 0.114*B

# Cropping the image
cropped_img = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

plt.figure(3)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")


plt.show()