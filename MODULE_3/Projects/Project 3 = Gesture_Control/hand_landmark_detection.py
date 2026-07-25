#Hand Landmark Detection
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error in accessing the webcam. Please try another one!")
    exit()

print("Hand Tracking has started! Press 'q' to quit.")

def detect_hand(hand_landmarks):
    landmarks = hand_landmarks.landmark
    extended = 0 
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 18]

    # Thumb Check - We compare the tip of thumb with the pip of Index Finger to find THUMB
    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[1]].x) > 0.04:
        extended += 1

    for i in range(1, 5):
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
            extended += 1

    if extended >= 4:
        return "Open"
    elif extended <= 1:
        return "Closed"
    else:
        return "Partial"

def drawing_by_index():
    


while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    gesture = "NO HAND DETECTED!!"

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Checking if the hand is left or right
            hand_label = results.multi_handedness[idx].classification[0].label
            # Detecting the Gesture using the function created
            gesture = detect_hand(hand_landmarks)
            # Drawing the connections (lines bw pips, tips, etc.) using 'draw_landmarks()'
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingertip_ids = [4,8,12,16,20]

            for tip_id in fingertip_ids:
                lm = hand_landmarks.landmark[tip_id]
                x, y = int(lm.x * w), int(lm.y * h)

                # Drawing circles on the tips
                cv2.circle(frame, (x, y), 10, (0,255,0), cv2.FILLED)
                cv2.putText(frame, str(tip_id), (x - 5, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

            # Wrist Location, and adding the text for Hand Label (Left or Right)
            wrist = hand_landmarks.landmark[0]
            wrist_x, wrist_y = int(wrist.x * w), int(wrist.y * h)
            cv2.putText(frame, f"{hand_label} Hand", (wrist_x - 40, wrist_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    status_color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

    cv2.imshow("Hand Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()