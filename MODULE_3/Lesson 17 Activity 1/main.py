# IMPORTS
import mediapipe as mp
import cv2
import time
import pyautogui

mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)
mp_draw = mp.solutions.drawing_utils

# CONFIGURATIONS
scroll_speed = 300
scroll_delay = 1
cam_width, cam_height = 640, 480

def detect_gesture(landmarks):
    # To detect whether palm is closed or open
    extended = 0
    TH, IX = mp_Hands.HandLandmark.THUMB_TIP, mp_Hands.HandLandmark.INDEX_FINGER_TIP

    # TO-DO: Check what is inside landmarks
    lm = landmarks.landmark
    print(landmarks)

    tips = [
        mp_Hands.HandLandmark.INDEX_FINGER_TIP,
        mp_Hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_Hands.HandLandmark.RING_FINGER_TIP,
        mp_Hands.HandLandmark.PINKY_TIP,
    ]

    if abs(lm[TH].x - lm[IX].x) > 0.04:
        extended += 1

    for tip in tips:
        if lm[tip].y < lm[tip-2].y:
            extended += 1

    #return "scroll_up" if extended == 5 else "scroll_down"
    if extended == 5:
        return "scroll_up"
    elif extended < 5:
        return "scroll_down"
    else:
        return None
    
cap = cv2.VideoCapture(0)

last_scroll_time = 0
while True:
    ret, frame = cap.read()

    if not cap.isOpened():
        print("Error: Webcam Not Accessible")
        exit()

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w = frame.shape[:2]
    gesture = "No hand detected"

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            hand_label = results.multi_handedness[idx].classification[0].label

            gesture = detect_gesture(hand_landmarks)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_Hands.HAND_CONNECTIONS)

            print(time.time() - last_scroll_time)
            
            if (time.time() - last_scroll_time) > scroll_delay:
                if gesture == "scroll_up":
                    pyautogui.scroll(scroll_speed)
                elif gesture =="scroll_down":
                    pyautogui.scroll(-scroll_speed)

                last_scroll_time = time.time()

            cv2.putText(frame, f"FPS:  | Hand: {hand_label} | Gesture: {gesture}", (10,30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()