import cv2
import mediapipe as mp
import random
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

choices = ['rock', 'paper', 'scissors']

def detect_move(landmarks):
    if not landmarks:
        return None

    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for id in range(1, 5):
        if landmarks[tip_ids[id]].y < landmarks[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    if fingers == [0, 0, 0, 0, 0]:
        return 'rock'
    elif fingers == [1, 1, 1, 1, 1]:
        return 'paper'
    elif fingers == [0, 1, 1, 0, 0]:
        return 'scissors'
    return None

def get_winner(user, ai):
    if user == ai:
        return "Draw"
    elif (user == 'rock' and ai == 'scissors') or \
         (user == 'paper' and ai == 'rock') or \
         (user == 'scissors' and ai == 'paper'):
        return "You Win!"
    else:
        return "AI Wins!"

cap = cv2.VideoCapture(0)
prev_move = None
ai_choice = None
result = ""
last_time = time.time()

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    move = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            move = detect_move(hand_landmarks.landmark)

    # Every 3 seconds, update the AI and result
    if time.time() - last_time > 3 and move:
        ai_choice = random.choice(choices)
        result = get_winner(move, ai_choice)
        prev_move = move
        last_time = time.time()

    # Display current state
    cv2.putText(frame, f"Your Move: {prev_move}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(frame, f"AI Move: {ai_choice}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    cv2.putText(frame, result, (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.putText(frame, "Show: Rock (fist), Paper (open), Scissors (2 fingers)", (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    cv2.imshow("AI Rock-Paper-Scissors", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
    