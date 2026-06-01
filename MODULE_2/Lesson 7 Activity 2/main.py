import cv2

image = cv2.imread("MODULE_2\Assets\Images\example.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (224, 224))

cv2.imshow("Resized Image in Grayscale", resized_image)

key = cv2.waitKey(0)
print(key)

if key == ord("s"):
    cv2.imwrite("MODULE_2/Lesson 7 Activity 2/grayscale_resized_image.jpg", resized_image)

else:
    print("Image not Saved")

cv2.destroyAllWindows()

print(f"Image Dimensions: {resized_image.shape}")