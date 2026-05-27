import cv2

image = cv2.imread("MODULE_2\Lesson 7 Activity 1\example.jpg")

window_name = "Loaded CV Window"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

cv2.resizeWindow(window_name, 800, 500)

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"Image Dimensions: {image.shape}")