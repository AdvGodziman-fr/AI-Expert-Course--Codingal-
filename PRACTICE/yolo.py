import cv2
import sys
from ultralytics import YOLO

model = YOLO("yolo26n.pt")

# Capturing Real-Time
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

    results = model(frame)
    annotated_frame = results[0].plot()

    # Display image in a window
    resized_image = cv2.resize(annotated_frame, (800, 400))

    cv2.imshow("Detections", resized_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
