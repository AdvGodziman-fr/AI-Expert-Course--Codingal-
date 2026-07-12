import cv2

class Keys:
    KEY_B = ord("b") # Blue tint
    KEY_G = ord("g") # Green Tint
    KEY_R = ord("r") # Red Tint
    KEY_I = ord("i") # Increase Red Intensity
    KEY_D = ord("d") # Decrease blue Intensity
    KEY_UPARROW = 2490368  # Increase Green Intensity (Doubt: How to use ord() to give values to the up_Arrow and down_Arrow keys?)
    KEY_DOWNARROW = 2621440 # Decrease Red Intensity
    KEY_Q = ord("q") # Quitting the Application

def apply_color_filter(image, filter_type):
    img = image.copy()

    if filter_type == "blue_tint":
        img[::1] = 0
        img[::2] = 0

    elif filter_type == "red_tint":
        img[::1] = 0
        img[::0] = 0

    elif filter_type == "green_tint":
        img[::0] = 0
        img[::2] = 0

    elif filter_type == "increase_red":
        


image = cv2.imread("MODULE_2/Projects/Project 5 = Real_Time_Color_Filtering/Img_for_filter.jpg")

better_img = cv2.resize(image, (1000, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)



while True:
    cv2.imshow("FIFA WC2026", better_img)
    cv2.waitKey(0) & 0xFF

    match :
        case 

