import cv2
import matplotlib.pyplot as plt

COLOR_WHITE = (255, 255, 255)
COLOR_PURPLE = (128, 0, 128)
COLOR_YELLOW = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_SKYBLUE = (135, 206, 235)
COLOR_ORANGE = (255, 140, 0)

img = cv2.imread("MODULE_2\Assets\Images\image.png")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Getting the width and height of the image
width, height = img_rgb.shape[0:2]

# Arrowed Line
arrow_start = (height - 20 , 20)
arrow_end = (height - 20, width - 25)

cv2.arrowedLine(img_rgb, arrow_start, arrow_end, COLOR_ORANGE, tipLength=0.02)
cv2.arrowedLine(img_rgb, arrow_end, arrow_start, COLOR_ORANGE, tipLength=0.02)

font = cv2.FONT_HERSHEY_SIMPLEX
height_label_pos = ((arrow_start[0]//2)-125, (arrow_start[1]+arrow_end[1])//2)

cv2.putText(img_rgb, f"Image Width: {width} px; Image Height: {height} px", height_label_pos, font, 0.5, COLOR_CYAN, 1, cv2.LINE_AA)


# Figure plotting and displaying
plt.figure(1)
plt.title("The Image")
plt.imshow(img_rgb)

# Functionalising the 's' key event
def call_backfun(event):
    if event.key == 's' or event.key =='S':
        plt.imsave("MODULE_2/Projects/Project 3 = Image_Annotations/Annotated_Image.png", img_rgb)
        plt.close('all')
        
    elif event.key == 'q':
        plt.close('all')

    else:
        print("Error, kindly press 'q' to quit or 's' to save.")

plt.figure(1).canvas.mpl_connect('key_press_event', call_backfun)

plt.show()