# BEGIN

# IMPORT OpenCV library as cv2
import cv2

# IMPORT NumPy as np
import numpy as np

import sys

class Keys:
    KEY_O = ord("o")
    KEY_R = ord("r")
    KEY_G = ord("g")
    KEY_B = ord("b")
    KEY_I = ord("i")
    KEY_D = ord("d")
    KEY_Q = ord("q")


def apply_color_filter(image, filter_type):
    """
    Apply a specific color filter to the given image and return the result.
    """
    filtered_image = image.copy()
    
    if filter_type == "red_tint":
        filtered_image[:,:,1] = 0
        filtered_image[:,:,0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:,:,1] = 0
        filtered_image[:,:,2] = 0
        #(Leaves only the blue channel visible)

    elif filter_type == "green_tint":
        #Blue channelt to 0
        filtered_image[:,:,0] = 0
        filtered_image[:,:,2] = 0
        #(Leaves only the green channel visible)

    elif filter_type == "increase_red":
        filtered_image[:,:,2] = cv2.add(filtered_image[:,:,2], 50)
        #(Ensures pixel values do not overflow beyond 255)

    elif filter_type == "decrease_blue":
        filtered_image[:,:,2] = cv2.subtract(filtered_image[:,:,2], 50)
        #(Ensures pixel values do not go below 0)

    return filtered_image


# # MAIN SCRIPT EXECUTION

# SET image_path = "example.jpg"   # File path of input image
image_path = "MODULE_2/Assets/Images/filter_photo.jpg"

# LOAD the image using cv2.imread
raw_image = cv2.imread(image_path)

# IF image could not be loaded:
#     EXIT & PRINT error message "Image not found!"
if raw_image is None:
    sys.exit("Error: Image not found!")

#     RESIZE the image to width=1200, height=800
image = cv2.resize(raw_image, (1200, 800))

#     INITIALIZE filter_type = "original"  # Default filter
filter_type = "original"

#     PRINT key options for the user:
#         o - Original
#         r - Red Tint
#         b - Blue Tint
#         g - Green Tint
#         i - Increase Red Intensity
#         d - Decrease Blue Intensity
#         q - Quit
print("Enter the following keys to apply the available filters: ")
print("o - Original")
print("r - Red Tint")
print("b - Blue Tint")
print("g - Green Tint")
print("i - Increase Red Intensity")
print("d - Decrease Blue Intensity")
print("q - Quit")

#     WHILE True (loop continuously until user exits):
#         CALL apply_color_filter(image, filter_type) → filtered_image
#         DISPLAY filtered_image in a window titled "Filtered Image"
while True:
    filtered_image = apply_color_filter(image, filter_type)

    cv2.imshow("Filtered Image", filtered_image)
#         WAIT for user key input
    key = cv2.waitKey(0) & 0xFF

    match key:
        case Keys.KEY_O:
            filter_type = "original"
        case Keys.KEY_R:
            filter_type = "red_tint"
        case Keys.KEY_B:
            filter_type = "blue_tint"
        case Keys.KEY_G:
            filter_type = "green_tint"
        case Keys.KEY_D:
            filter_type = "decrease_blue"
        case Keys.KEY_I:
            filter_type = "increase_red"
        case Keys.KEY_Q:
            break
        case _:
            print("Invalid key! Please use 'o', 'r', 'b', 'g', 'i', 'd', or 'q'.")

#     CLOSE all OpenCV windows
cv2.destroyAllWindows()
# END
