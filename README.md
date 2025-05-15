AI Rock-Paper-Scissors Game Using Hand Gesture Recognition
Project Overview
This project implements a real-time Rock-Paper-Scissors game that leverages computer vision and artificial intelligence techniques to recognize hand gestures from a webcam feed. Using MediaPipe for hand landmark detection and OpenCV for image processing, the system detects the player's hand sign (rock, paper, or scissors) and pits it against an AI opponent that randomly selects its move. The game then determines the winner and displays the result instantly.

FeaturE
Real-time hand gesture detection using MediaPipe Hands.

Recognition of three gestures: Rock, Paper, and Scissors.

AI opponent randomly chooses a move.

Immediate result display: Player win, AI win, or tie.

Interactive and user-friendly interface with live webcam feed.

Visual feedback showing detected gestures and results.

Technologies Used
Python 3.10

OpenCV (Open Source Computer Vision Library)

MediaPipe (Google’s framework for building perception pipelines)

NumPy

How It Works
Hand Landmark Detection: The system captures video from the webcam and processes each frame to detect hand landmarks using MediaPipe.

Gesture Classification: Based on landmark positions, the code determines whether the player’s hand shows rock, paper, or scissors.

AI Move: The AI randomly selects a move.

Winner Decision: The game compares the player’s and AI’s moves to decide the winner.

Display: The result and the moves are displayed on the screen in real-time.

Installation & Running Instructions
Ensure Python 3.10 is installed.

Install required packages using pip:

nginx
Copy
Edit
pip install opencv-python mediapipe numpy
Run the main script:

nginx
Copy
Edit
python rock_paper_scissors.py
Use your hand in front of the webcam to play. Press Esc to exit.

Future Improvements
Add support for more gestures or multiplayer mode.

Improve AI by incorporating learning-based strategies.

Enhance UI with better graphics and scorekeeping.

Integrate audio feedback for better interactivity.

License
This project is open-source and free to use for educational purposes.
