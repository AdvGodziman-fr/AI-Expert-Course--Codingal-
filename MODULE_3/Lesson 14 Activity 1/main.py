import cv2

# Code for ResNet SSD (Single Shot-Multibox Detector)
RESNET_CONFIG = r"MODULE_2\Assets\Documents\deploy.prototxt"
PRE_TRAINED_MODEL = r"MODULE_2\Assets\Documents\res10_300x300_ssd_iter_140000.caffemodel"


def main():
    cap = cv2.imread(r"MODULE_2\Assets\Images\image.png")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break

        # Load the pre-trained deep learning face detection model
        net = cv2.dnn.readNet(
            config=RESNET_CONFIG, model=PRE_TRAINED_MODEL)

        h, w = frame.shape[:2]

        # Prepare the image for the neural network (blobbing)
        blob = cv2.dnn.blobFromImage(cv2.resize(
            frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()

        # Loop over the detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:  # Filter out weak detections
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY),
                              (endX, endY), (0, 255, 0), 2)

        cv2.imshow("Filter", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

