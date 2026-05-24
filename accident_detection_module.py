import random
import time
import math
from datetime import datetime

# -----------------------------
# Configuration Parameters
# -----------------------------
ACCIDENT_THRESHOLD = 3.0   # g-force threshold
SAMPLING_TIME = 1          # seconds

# -----------------------------
# Initial State
# -----------------------------
system_state = "NORMAL"

print("\n🚗 Digital Twin – Accident Detection & Alert Logic Started\n")

# -----------------------------
# Main Loop
# -----------------------------
while True:
    # Virtual Accelerometer Data
    ax = random.uniform(-1.0, 1.0)
    ay = random.uniform(-1.0, 1.0)
    az = random.uniform(8.5, 10.5)  # gravity component

    # Resultant Acceleration (Magnitude)
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    # Display Sensor Data
    print(f"Ax: {ax:.2f}g | Ay: {ay:.2f}g | Az: {az:.2f}g | "
          f"Magnitude: {magnitude:.2f}g", end="  ")

    # -----------------------------
    # Accident Detection Logic
    # -----------------------------
    if magnitude > ACCIDENT_THRESHOLD:
        system_state = "ACCIDENT"
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        print("\n🚨 ACCIDENT DETECTED 🚨")
        print(f"📍 Time: {timestamp}")
        print("📨 Sending emergency alert...")
        print("📞 Simulating emergency call...\n")

        break  # Stop after accident detection

    else:
        system_state = "NORMAL"
        print("Status: NORMAL")

    time.sleep(SAMPLING_TIME)