import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r"MODULE_2\Assets\Images\ex_img_L8.jpg")
if image is None:
    print("Error: Could not load image. Check your file path!")
    raise SystemExit

img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cropping the image
cropped_rgb = img_rgb[100:1000, 200:2000]

# Rotating the image
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_rgb = cv2.warpAffine(img_rgb, M, (w, h))

# Brightening the image
brightness_matrix = np.ones(img_rgb.shape, dtype="uint8") * 50
brighter_rgb = cv2.add(img_rgb, brightness_matrix)

# Image Interpolation
downscaled_img = cv2.resize(img_rgb, (0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
upscaled_img = cv2.resize(img_rgb, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_LANCZOS4)
diff_up_img = cv2.resize(img_rgb, (0, 0), fx=9.0, fy=10.0, interpolation=cv2.INTER_CUBIC)

# --- FIGURES ---
plt.figure(1)
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")

plt.figure(2)
plt.imshow(cropped_rgb)
plt.title("Cropped RGB Image")

plt.figure(3)
plt.imshow(rotated_rgb)
plt.title("Rotated RGB Image")

plt.figure(4)
plt.imshow(brighter_rgb)
plt.title("Brightened RGB Image")

plt.figure(5)
plt.imshow(downscaled_img)
plt.title("Interpolated Image (INTER_AREA)")

plt.figure(6)
plt.imshow(upscaled_img)
plt.title("Interpolated Image (LANCZOS4)")

plt.figure(7)
plt.imshow(diff_up_img)
plt.title("Interpolated Image (CUBIC)")


# Key handler function
def on_key(event):
    if event.key == 's':
        img_gray_bgr = img_gray  # Grayscale doesn't need color conversion
        cropped_bgr = cv2.cvtColor(cropped_rgb, cv2.COLOR_RGB2BGR)
        rotated_bgr = cv2.cvtColor(rotated_rgb, cv2.COLOR_RGB2BGR)
        brighter_bgr = cv2.cvtColor(brighter_rgb, cv2.COLOR_RGB2BGR)
        
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/grayscale_image.jpg", img_gray_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/cropped_image.jpg", cropped_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/rotated_image.jpg", rotated_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/brightened_image.jpg", brighter_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/downscaled_INTERAREA.jpg", downscaled_img)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/upscaled_INTERLANCZOS.jpg", upscaled_img)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/upscaled_INTERCUBIC.jpg", diff_up_img)

        print("Images saved successfully!")
    else:
        print(f"Key '{event.key}' pressed. Images not saved!")
    
    plt.close('all')


# THE FIX: Connect the key listener to every active figure window
for fig_num in [1, 2, 3, 4, 5, 6, 7]:
    plt.figure(fig_num).canvas.mpl_connect('key_press_event', on_key)

# Display everything
plt.show()