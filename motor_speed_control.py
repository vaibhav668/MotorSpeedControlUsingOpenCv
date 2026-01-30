import cv2
import mediapipe as mp
import serial
import time
import math
import numpy as np

arduino = serial.Serial('COM5', 9600, timeout=1)  
time.sleep(2)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)


prev_speed = 0
def smooth(current, prev, alpha=0.2):
    return int(prev + alpha * (current - prev))


def draw_panel(img, x, y, w, h, alpha=0.4):
    overlay = img.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (20, 20, 20), -1)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

def glow_line(img, p1, p2, color):
    for i in range(6, 0, -1):
        cv2.line(img, p1, p2, color, i * 2)


NEON_PINK = (255, 0, 255)
NEON_CYAN = (255, 255, 0)
NEON_MINT = (0, 255, 180)


while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    speed = 0

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark

            x1, y1 = int(lm[4].x * w), int(lm[4].y * h)
            x2, y2 = int(lm[8].x * w), int(lm[8].y * h)

          
            dist = int(math.hypot(x2 - x1, y2 - y1))

            
            dist = np.clip(dist, 30, 200)
            raw_speed = np.interp(dist, [30, 200], [0, 255])
            speed = smooth(int(raw_speed), prev_speed)
            prev_speed = speed

            arduino.write(f"{speed}\n".encode())

            
            glow_color = (255 - speed, speed, 255)
            glow_line(frame, (x1, y1), (x2, y2), glow_color)

            cv2.circle(frame, (x1, y1), 10, NEON_PINK, -1)
            cv2.circle(frame, (x2, y2), 10, NEON_PINK, -1)

        
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(frame, (mid_x, mid_y),
                       20 + speed // 25, glow_color, 2)

            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)


    draw_panel(frame, 30, h - 130, 380, 100)

    bar_width = int((speed / 255) * 300)
    cv2.rectangle(frame, (50, h - 90),
                  (50 + bar_width, h - 60), NEON_MINT, -1)
    cv2.rectangle(frame, (50, h - 90),
                  (350, h - 60), (100, 100, 100), 2)

    cv2.putText(frame, "MOTOR SPEED",
                (50, h - 100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, NEON_CYAN, 2)

    cv2.putText(frame, f"{int(speed / 255 * 100)}%",
                (360, h - 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, NEON_CYAN, 2)

    cv2.imshow("Gesture Motor Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
