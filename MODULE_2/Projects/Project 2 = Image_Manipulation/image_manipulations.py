import cv2 
import matplotlib.pyplot as plt 
import numpy as np  

# --- IMAGE LOADING & ERROR HANDLING ---
# Load the image from the specified path. OpenCV reads images in BGR format by default.
image = cv2.imread(r"MODULE_2\Assets\Images\ex_img_L8.jpg")

# Check if the image was successfully loaded. If the path is wrong, 'image' will be None.
if image is None:
    print("Error: Could not load image. Check your file path!")
    raise SystemExit  # Terminate the program immediately if the image cannot be found

# --- COLOR SPACE CONVERSIONS ---
# Convert the image from BGR (OpenCV default) to RGB so Matplotlib displays the colors correctly.
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the original BGR image to Grayscale (black and white).
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --- IMAGE MANIPULATION ---

# 1. Cropping the image
# Uses NumPy slicing to crop. Format: [start_y:end_y, start_x:end_x]
# This extracts a specific rectangular region from the RGB image.
cropped_rgb = img_rgb[100:1000, 200:2000]

# 2. Rotating the image
# Get the height (h) and width (w) from the first two elements of the image shape tuple.
(h, w) = image.shape[:2]
# Calculate the center coordinate of the image using integer division (//).
center = (w // 2, h // 2)
# Generate a 2D rotation matrix: center point, angle (45 degrees counter-clockwise), and scale factor (1.0 = no scaling).
M = cv2.getRotationMatrix2D(center, 45, 1.0)
# Apply the transformation matrix to rotate the image. (w, h) sets the size of the output canvas.
rotated_rgb = cv2.warpAffine(img_rgb, M, (w, h))

# 3. Brightening the image
# Create a matrix of the same shape/size as the image filled with 1s, multiplied by 50.
# "uint8" ensures the data type matches standard 8-bit image pixels (0-255).
brightness_matrix = np.ones(img_rgb.shape, dtype="uint8") * 50
# Use cv2.add() to add 50 to every pixel channel. OpenCV automatically caps values at 255 to prevent overflow.
brighter_rgb = cv2.add(img_rgb, brightness_matrix)

# 4. Image Interpolation (Resizing)
# Downscale the image to 10% (fx=0.1, fy=0.1) of its size. INTER_AREA is ideal for shrinking images.
downscaled_img = cv2.resize(img_rgb, (0, 0), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)

# Upscale the image to 250% (fx=2.5, fy=2.5). INTER_LANCZOS4 is a high-quality, complex resizing algorithm.
upscaled_img = cv2.resize(img_rgb, (0, 0), fx=2.5, fy=2.5, interpolation=cv2.INTER_LANCZOS4)

# Stretch/upscale the image unevenly (9x horizontally, 10x vertically). INTER_CUBIC uses a 4x4 pixel neighborhood.
diff_up_img = cv2.resize(img_rgb, (0, 0), fx=9.0, fy=10.0, interpolation=cv2.INTER_CUBIC)


# --- CREATING FIGURES WITH MATPLOTLIB ---
# Each block opens a new numbered window, displays an image, and gives it a title.

plt.figure(1)
plt.imshow(img_gray, cmap='gray')  # cmap='gray' tells Matplotlib to render it as a true grayscale image
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


# --- EVENT HANDLING & SAVING ---

# Define a callback function that executes whenever a key is pressed inside a figure window.
def on_key(event):
    # Check if the pressed key is 's' (for save)
    if event.key == 's':
        img_gray_bgr = img_gray  # Grayscale images have only 1 channel, no color conversion needed
        
        # Convert RGB images back to BGR before saving, because cv2.imwrite expects BGR format.
        cropped_bgr = cv2.cvtColor(cropped_rgb, cv2.COLOR_RGB2BGR)
        rotated_bgr = cv2.cvtColor(rotated_rgb, cv2.COLOR_RGB2BGR)
        brighter_bgr = cv2.cvtColor(brighter_rgb, cv2.COLOR_RGB2BGR)
        
        # Save all processed images to the specified folder paths
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/grayscale_image.jpg", img_gray_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/cropped_image.jpg", cropped_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/rotated_image.jpg", rotated_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/brightened_image.jpg", brighter_bgr)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/downscaled_INTERAREA.jpg", downscaled_img)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/upscaled_INTERLANCZOS.jpg", upscaled_img)
        cv2.imwrite("MODULE_2/Projects/Project 2 = Image_Manipulation/output_images/upscaled_INTERCUBIC.jpg", diff_up_img)

        print("Images saved successfully!")
    else:
        # Inform the user that a different key was pressed and saving was skipped
        print(f"Key '{event.key}' pressed. Images not saved!")
    
    # Close all active Matplotlib plot windows after a keypress action completes
    plt.close('all')


# Loop through figures 1 through 7 and link the 'key_press_event' to our 'on_key' function.
# This ensures that pressing 's' works no matter which image window is currently selected.
for fig_num in [1, 2, 3, 4, 5, 6, 7]:
    plt.figure(fig_num).canvas.mpl_connect('key_press_event', on_key)

# Render and display all the created figures on the screen. Execution pauses here until windows are closed.
plt.show()