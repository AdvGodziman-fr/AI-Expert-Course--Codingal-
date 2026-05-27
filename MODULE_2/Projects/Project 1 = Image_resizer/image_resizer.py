import cv2

image = cv2.imread("MODULE_2/Projects/Project 1 = Image_resizer/example.jpg")

# Check if image loaded correctly before proceeding
if image is None:
    print("Error: Could not load the image. Check your file path!")
    exit()

window_name1 = "Image Resizer - A CV Tool"
window_name2 = "Image Resizer 2"
window_name3 = "Image Resizer 3"

cv2.namedWindow(window_name1, cv2.WINDOW_NORMAL)
cv2.namedWindow(window_name2, cv2.WINDOW_NORMAL)
cv2.namedWindow(window_name3, cv2.WINDOW_NORMAL)

small = (200, 200)
medium = (400, 400)
large = (600, 600)


def resizer(window_name, size):
    # FIX: Use cv2.resize to actually change the image pixel dimensions
    resized_img = cv2.resize(image, size)
    cv2.imshow(window_name, resized_img)

    return resized_img


small_img = resizer(window_name1, small)
mid_img = resizer(window_name2, medium)
large_img = resizer(window_name3, large)


print("If you press 's', all the three images would be saved to your folder.")

key = cv2.waitKey(0)

# FIX: Used forward slashes to avoid Windows backslash string escaping issues
if key == ord("s"):
    cv2.imwrite(
        "MODULE_2/Projects/Project 1 = Image_resizer/small_img.jpg", small_img
    )
    cv2.imwrite(
        "MODULE_2/Projects/Project 1 = Image_resizer/medium_img.jpg", mid_img
    )
    cv2.imwrite(
        "MODULE_2/Projects/Project 1 = Image_resizer/large_img.jpg", large_img
    )
    print("Images saved successfully!")
else:
    print("Images will not be saved!")

cv2.destroyAllWindows()

print(f"Image Dimensions of Small Image: {small_img.shape}")
print(f"Image Dimensions of Medium-sized Image: {mid_img.shape}")
print(f"Image Dimensions of Large Image: {large_img.shape}")