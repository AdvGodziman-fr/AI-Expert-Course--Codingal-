# Volume and Brightness control 
import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

# TASK-1 : MediaPipe Hand Setup and Fingertip Landmark Detection
Hands = mp.solutions.hands

hands = Hands.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)

draw = mp.solutions.drawing_utils

TH, IX = Hands.HandLandmark.THUMB_TIP, Hands.HandLandmark.INDEX_FINGER_TIP

# TASK - 2: Setting up a system volume control
try:
    if hasattr(AudioUtilities, "GetDefaultOutputDevice"):
        device = AudioUtilities.GetDefaultOutputDevice()

    else:
        device = AudioUtilities.GetSpeakers()

    vol_ctrl = device.EndpointVolume.QueryInterface(IAudioEndpointVolume)
    minv, maxv = vol_ctrl.GetVolumeRange()[:2]

except Exception as e:
    print(e)
    exit()

# TASK - 3: Webcam Access
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam Not Accessible")
    exit()

window_title = "Hand Gesture Control"

cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)

# TASK - 4: Main Loop to Read Camera Frames (Hand Detection)
while True:
    ok, img = cap.read()

    if not ok:
        break

    img = cv2.flip(img, 1)
    h, w = img.shape[:2]

    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # TASK 5: Checking Detected Hands and getting left/right labels
    if res.multi_hand_landmarks and res.multi_handedness:
        for i, hand in enumerate(res.multi_hand_landmarks):
            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)
            label = res.multi_handedness[i].classification[0].label
            print(label)

        # TASK 6: Fingertip Coordinate extraction and distance measurement
            lm = hand.landmark
            tp = (int(lm[TH].x * w), int(lm[TH].y * h))
            ip = (int(lm[IX].x * w), int(lm[IX].y * h))

            # Draw circles on both tips
            cv2.circle(img, tp, 10, (255,0,0), cv2.FILLED)
            cv2.circle(img, ip, 10, (255,0,0), cv2.FILLED)

            # Draw a line between the tips
            cv2.line(img, tp, ip, (0,255,0), 3)

            # Calculate the distance
            distance = float(np.hypot(ip[0] - tp[0], ip[1] - tp[1]))

            # TASK - 7: Volume Control 
            if label == "Left": 
                v = np.interp(distance, [30, 300], [minv, maxv])
                try:
                    vol_ctrl.SetMasterVolumeLevel(v, None)
                except Exception as e:
                    print("Error in volume control: ", e)

                bar = int(np.interp(distance, [30,300], [400,150]))
                pct = int(np.interp(distance, [30,300], [0,100]))

                cv2.rectangle(img, (50,150), (85,400), (255,0,0), 2) 
                cv2.rectangle(img, (50,bar), (85,400), (255,0,0), cv2.FILLED)
                cv2.putText(img, f"{pct}%", (40,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

            # TASK - 8: Brightness Control
            elif label == "Right":
                pass

        cv2.imshow(window_title, img)
        k = cv2.waitKey(1) & 0xFF
        if k in (27, ord("q")):
            break

cap.release()
cv2.destroyAllWindows()