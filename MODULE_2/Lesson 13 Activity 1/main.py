import cv2
import sys

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Capture frame-by-frame
frame = cv2.imread("MODULE_2/Assets/Images/image.png")

# Convert frame to grayscale (Face detection works better on grayscale)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 4, minSize=(25, 25))

# Draw rectangles around the faces\
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x , y), (x + w, y + h), (255, 0, 0), 2)

    # Creating a Region of Interest
    roi_img = frame[y:y+h, x:x+w]
    roi_gray_img = gray[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray_img, minNeighbors=4)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_img, (ex , ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.namedWindow("Detected-Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Detected-Image", 500, 750)
cv2.imshow("Detected-Image", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()