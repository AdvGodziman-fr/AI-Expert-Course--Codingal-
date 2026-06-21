import cv2
import numpy as np
import matplotlib.pyplot as plt

"""Utility function to display an image"""
def display_image(title, image, original):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 16))

    ax1.imshow(original)
    ax1.set_title("Original Image")

    if len(image.shape) == 2:
        ax2.imshow(image, cmap='gray')
    else:
        ax2.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

"""Interactive activity for edge detection and filtering"""
def interactive_edge_detection(image_path):
    # TODO: Load the image
    image = cv2.imread(filepath)

    # TODO: Please show error if no image found
    if image is None:
        print("Image Not Found!")
        return 
    
    # TODO: Convert to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image("Original Image", img_gray, img)

    print("Select an option: ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Blur")
    print("5. Median Blur")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        # SOBEL EDGE DETECTION
        if choice == "1":
            sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
            abs_sobelx = cv2.convertScaleAbs(sobel_x)
            abs_sobely = cv2.convertScaleAbs(sobel_y)

            combined_sobel = cv2.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)

            display_image("Sobel Edge Applied", combined_sobel, img)

        # CANNY EDGE DETECTION
        elif choice == "2":
            lower_threshold = int(input("Enter lower threshold: ") or 100)
            upper_threshold = int(input("Enter upper threshold: ") or 200)

            canny_img = cv2.Canny(img_gray, lower_threshold, upper_threshold)

            display_image("Canny Edge Applied", canny_img, img)
            
        
        # LAPLACIAN EDGE DETECTION
        elif choice == "3":
            lap_img = cv2.Laplacian(img_gray, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(lap_img).astype(np.uint8), img)

        # GAUSSIAN SMOOTHING
        elif choice == "4":
            kernel_size = int(input("Please enter the kernel size (must be odd): "))

            blurred_img_1 = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

            display_image("Gaussian Blurred Image", blurred_img_1, img)

        # MEDIAN FILTERING
        elif choice == "5":
            kernel_size = int(input("Please enter the kernel size (must be odd): "))

            blurred_img_2 = cv2.medianBlur(img, kernel_size)

            display_image("Median Blurred Image", blurred_img_2, img)
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


# Please replace your image file relative path below
filepath = "MODULE_2/Assets/Images/ex_img_L8.jpg"
interactive_edge_detection(filepath)