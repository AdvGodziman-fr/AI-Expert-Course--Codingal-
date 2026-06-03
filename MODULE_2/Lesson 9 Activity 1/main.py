import cv2
import matplotlib.pyplot as plt

COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (128, 0, 128)
COLOR_YELLOW = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_SKYBLUE = (135, 206, 235)
COLOR_ORANGE = (255, 140, 0)

image_path = "MODULE_2/Assets/Images/image_exp.jpg"

# Reads the image from the specified path
image = cv2.imread(image_path)

# Convert the image from OpenCV’s default BGR format to RGB for accurate color display with matplotlib.
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Retrieves the dimensions of the image.
height, width, _ = image_rgb.shape



# _____________________________________________________________________________________
# TASK 1 : DRAW A RECTANGLE IN THE TOP-LEFT CORNER OF THE IMAGE

# Specifies the width and height of the rectangle.
rect1_height, rect1_width = 150, 150

# Fixed 20 pixels padding from top-left
top_left1 = (20, 20)

# Calculates the bottom-right corner coordinates based on the width and height.
bottom_right1 = (top_left1[0] + rect1_height, top_left1[1] + rect1_width)

# Draw a Yellow-bordered rectangle - color is in BGR format
cv2.rectangle(image_rgb, top_left1, bottom_right1, COLOR_SKYBLUE, 3)


# _____________________________________________________________________________________
# TASK 2 : DRAW A RECTANGLE IN THE BOTTOM-RIGHT CORNER OF THE IMAGE

# Specifies the width and height of the rectangle.
rect2_height, rect2_width = 200, 150

# Fixed 20 pixels padding from top-left
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)

# Calculates the bottom-right corner coordinates based on the width and height.
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)

# Draw a Yellow-bordered rectangle - color is in BGR format
cv2.rectangle(image_rgb, top_left2, bottom_right2, COLOR_YELLOW, 3)


# _____________________________________________________________________________________
# TASK 3 : DRAW FILLED-IN CIRCLES IN THE CENTERS OF THE ABOVE RECTANGLES

# Calculate center 1 for the 1st circle
center1 = (rect1_width//2 + top_left1[0], rect1_height//2 + top_left1[1])

# Draw a filled Green cicle
cv2.circle(image_rgb, center1, 15, COLOR_PURPLE, -1)

# Calculate center 1 for the 1st circle
center2 = (rect2_width//2 + top_left2[0], rect2_height//2 + top_left2[1])

# Draw a filled Green cicle
cv2.circle(image_rgb, center2, 15, COLOR_PURPLE, -1)


# _____________________________________________________________________________________
# TASK 4: DRAW A LINE CONNECTING THE 2 CENTERS
cv2.line(image_rgb, center2, center1, COLOR_CYAN, 3)


# _____________________________________________________________________________________
# TASK 5: DRAW A LINE CONNECTING THE 2 CENTERS
# Label the rectangles and centers with descriptive text.
# Position text just above the rectangle for visibility.

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(image_rgb, "Region 1", (top_left1[0], top_left1[1] + rect1_height + 30), font, 0.7, COLOR_SKYBLUE, 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Region 2", (top_left2[0], top_left2[1] - 30), font, 0.7, COLOR_SKYBLUE, 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Center 1", (center1[0] - 40, center1[1] - 40), font, 0.6, COLOR_SKYBLUE, 2, cv2.LINE_AA)
cv2.putText(image_rgb, "Center 2", (center2[0] - 40, center2[1] + 40), font, 0.6, COLOR_SKYBLUE, 2, cv2.LINE_AA)

# _____________________________________________________________________________________
# TASK 6: DRAW A BI-DIRECTIONAL ARROW (2 ARROWED LINES) TO MARK THE HEIGHT OF THE IMAGE

# Draw bi-directional arrows
arrow_start = (width - 50, 20) # Start near the top right
arrow_end = (width - 50, height - 20) # End near the bottom right

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, COLOR_YELLOW, 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, COLOR_YELLOW, 3, tipLength=0.05)


# _____________________________________________________________________________________
# TASK 7: ADD TEXT TO THE LINE WITH DYNAMIC TEXT SHOWING HEIGHT OF IMAGE

height_label_pos = (arrow_start[0] - 255, (arrow_start[1] + arrow_end[1]) // 2)

cv2.putText(image_rgb, f"Height: {height} px", height_label_pos, font, 0.9, COLOR_CYAN, 2, cv2.LINE_AA)



plt.imshow(image_rgb)
plt.title("Annotated image with regions, centers, bi-directional arrow")
plt.axis("off")
plt.show()