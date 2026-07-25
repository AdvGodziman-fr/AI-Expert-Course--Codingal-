import cv2
import os

RESNET_CONFIG = r"MODULE_3\Assets\Documents\deploy.prototxt"
PRE_TRAINED_MODEL = r"MODULE_3\Assets\Documents\res10_300x300_ssd_iter_140000.caffemodel"
IMAGE_PATH = r"MODULE_3\Assets\Images\image.png"


def main():
    if not os.path.exists(RESNET_CONFIG) or not os.path.exists(PRE_TRAINED_MODEL):
        print("Model files not found.")
        return

    frame = cv2.imread(IMAGE_PATH)
    if frame is None:
        print(f"Could not load image: {IMAGE_PATH}")
        return

    net = cv2.dnn.readNet(config=RESNET_CONFIG, model=PRE_TRAINED_MODEL)

    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        scalefactor=1.0,
        size=(300, 300),
        mean=(104.0, 177.0, 123.0)
    )

    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = float(detections[0, 0, i, 2])
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (startX, startY, endX, endY) = box.astype("int")

            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = f"{confidence * 100:.1f}%"
            text_y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.putText(frame, label, (startX, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.45, (0, 255, 0), 2)

    cv2.imshow("Filter", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()