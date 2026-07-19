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

    # Thumb 
    if abs(landmarks)

while True:
    ret, frame = cap.read()