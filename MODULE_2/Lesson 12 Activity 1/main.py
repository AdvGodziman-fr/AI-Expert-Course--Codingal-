import cv2
import sys

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Start video capture from the default webcam (0)
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    sys.exit("Camera not found")

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    # If frame is read correctly, ret will be True
    if not ret:
        print("Error: Failed to capture image!")
        break

    # Convert frame to grayscale (Face detection works better on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize=(30, 30))

    # Draw rectangles around the faces\
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x , y), (x + w, y + h), (255, 0, 0), 2)

        # Creating a Region of Interest
        roi_img = frame[y:y+h, x:x+w]
        roi_gray_img = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray_img, minNeighbors=5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (ex , ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Face Detection - press q to Quit", frame)

    # Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the capture and close any open windows
capture.release()
cv2.destroyAllWindows()