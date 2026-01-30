✋ Gesture Controlled Motor Speed using OpenCV

This project controls the speed of a DC motor using hand gestures captured from a webcam.
The distance between two fingers (thumb and index) is detected using computer vision, and the motor speed changes in real time.

No buttons. No remote. Just your hand.

🚀 Features

Two-finger (pinch) gesture to control motor speed

Real-time hand tracking using webcam

Smooth motor speed control using PWM

Clean and interactive OpenCV visualization

Works with Arduino + DC motor

🛠️ Tech Stack

Python

OpenCV

MediaPipe

Arduino

L298N Motor Driver

🔌 Hardware Required

Arduino UNO / Nano

DC Motor (fan recommended for visible speed)

L298N or L293D Motor Driver

External power supply (9–12V)

Jumper wires

USB cable (data cable)

🔗 Circuit Connections
L298N → Arduino
L298N Pin	Arduino Pin
ENA	D9 (PWM)
IN1	D8
IN2	D7
GND	GND
+12V	External Power +
OUT1 / OUT2	DC Motor

⚠️ Make sure:

ENA jumper is removed

Arduino and motor driver share common ground

💻 Software Setup (VS Code)
1️⃣ Install Python

Download from: https://www.python.org

✔ Make sure “Add Python to PATH” is checked during installation.

Check installation:

python --version

2️⃣ Open Project in VS Code

Open VS Code

File → Open Folder → select project folder

3️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate

4️⃣ Install Required Libraries
pip install opencv-python mediapipe pyserial numpy


That’s it. No extra setup needed.

🧑‍💻 Arduino Setup

Open Arduino IDE

Select correct board and COM port

Upload the Arduino code provided in this repo

Close Arduino Serial Monitor (important)

▶️ How to Run

Connect Arduino to PC

Connect motor driver and motor

Update COM port in Python file if needed

Run the Python script:

python gesture_motor_final.py


Show your hand to the camera

Move thumb and index finger closer/farther

Motor speed changes in real time ⚙️
