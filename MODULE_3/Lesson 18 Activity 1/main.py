import cv2, time, numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands

tip_ids = {
    "thumb": mp_hands.HandLandmark.THUMB_TIP,
    "index": mp_hands.HandLandmark.INDEX_FINGER_TIP,
    "middle": mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
    "ring": mp_hands.HandLandmark.RING_FINGER_TIP,
    "pinky": mp_hands.HandLandmark.PINKY_TIP,
}

hands = mp_hands.Hands(
    min_detection_confidence = 0.7,
    min_tracking_confidence = 0.7
)

mp_draw = mp.solutions.drawing_utils

pairs = {
    "middle": ("SEPIA", "NEGATIVE"),
    "ring": ("BLUR", "GLITCH"),
    "pinky": ("EDGE", "CARTOON")
}

current_filter = "SEPIA"

tracker = {k: 0 for k in pairs}

# Capital Letters - Constants
DEBOUNCE = 2.5
CAPTURE_THRES_TIME = 2.0
TT = 30
TP = 20

last_action = 0
last_capture = 0
pinch_on = False


MAIN_TITLE = "Gesture-Controlled Photo App"
POPOUT_WINDOW = "Captured (Press ESC to close)"

paused = False
freeze = None

SEPIA_M = np.array([[0.272,0.534,0.131],[0.349,0.686,0.168],[0.393,0.769,0.189]])

# Apply the filters to the web-cam frame
def apply(img, t):
    if t == "SEPIA": return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8)
    if t == "NEGATIVE": return cv2.bitwise_not(img)
    if t == "BLUR": return cv2.GaussianBlur(img, (15, 15), 0)
    if t == "GLITCH":
        h,w = img.shape[:2]; r,g,b = img[:,:,2], img[:,:,1], img[:,:,0]
        return cv2.merge([np.roll(b, -int(0.02*w), 1), g, np.roll(r, int(0.04*w), 1)])
    if t == "EDGE": return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160)
    if t == "CARTOON":
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        e = cv2.adaptiveThreshold(cv2.medianBlur(g, 7), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        c = cv2.bilateralFilter(img, 9, 75, 75)
        return cv2.bitwise_and(c, c, mask=e)
    return img

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam Not Accessible")
    exit()

cv2.namedWindow(MAIN_TITLE, cv2.WINDOW_NORMAL)

while True:
    if paused:
        cv2.imshow(MAIN_TITLE, freeze)
        k = cv2.waitKey(1) & 0xFF
        if k == ord("q"):
            break
        if k == 27:
            paused = False
            pinch_on = False

            cv2.destroyWindow(POPOUT_WINDOW)
            continue

        try:
            if cv2.getWindowProperty(POPOUT_WINDOW, cv2.WND_PROP_VISIBLE) <= 0: 
                paused = False
                pinch_on = False
        except cv2.error:
            paused = False
            pinch_on = False
        continue

    ret, img = cap.read()

    if not ret:
        print("Error! Couldn't capture image.")
        exit()

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w = img.shape[:2]

    now = time.time()
    capture = False

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)
        lm = hand.landmark

        tips = {k:(int(lm[v].x*w), int(lm[v].y*h)) for k,v in tip_ids.items()}

        tx,ty = tips["thumb"]
        ix,iy = tips["index"]

        pinch = abs(tx - ix) < TP and abs(ty - iy) < TP

        if pinch and not pinch_on and now - last_capture > CAPTURE_THRES_TIME:
            pinch_on = True
            capture = True
            last_capture = now

        elif not pinch:
            if pinch_on:
                pinch_on = False

        t = next((k for k in pairs if abs(tx-tips[k][0]) < TT and abs(ty-tips[k][1]) < TT), None)

        if t and now - last_action > DEBOUNCE:
            current_filter = pairs[t][tracker[t]] 
            tracker[t] ^= 1
            last_action = now
            print("Current Filter: ", current_filter)          

    output = apply(img, current_filter)

    if current_filter == "EDGE":
        output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    if capture:
        name = f"Picture_{int(now)}.jpg"
        print("Saved: ", name)
        cv2.imwrite(name, output)
        paused = True
        freeze = output.copy()
        cv2.imshow(POPOUT_WINDOW, freeze)

    cv2.imshow(MAIN_TITLE, output)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()