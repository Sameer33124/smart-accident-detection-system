# -------------------------------
# MODULE 5 : DIGITAL TWIN ACCIDENT DETECTION
# Clean version (NO Streamlit)
# -------------------------------

import random
import time
from datetime import datetime

# Threshold values
ACCELERATION_THRESHOLD = 7.0   # g-force
TILT_THRESHOLD = 60            # degrees

def generate_sensor_data():
    """
    Simulates real-time sensor values
    """
    acceleration = round(random.uniform(0, 10), 2)
    tilt_angle = random.randint(0, 90)
    heart_rate = random.randint(60, 120)

    return acceleration, tilt_angle, heart_rate

def detect_accident(acceleration, tilt_angle):
    """
    Accident detection logic
    """
    if acceleration > ACCELERATION_THRESHOLD or tilt_angle > TILT_THRESHOLD:
        return True
    return False

def digital_twin_display(acceleration, tilt_angle, heart_rate, accident):
    """
    Displays digital twin status
    """
    print("\n==============================")
    print(" DIGITAL TWIN VEHICLE STATUS ")
    print("==============================")
    print(f"Time           : {datetime.now().strftime('%H:%M:%S')}")
    print(f"Acceleration   : {acceleration} g")
    print(f"Tilt Angle     : {tilt_angle}°")
    print(f"Heart Rate     : {heart_rate} BPM")

    if accident:
        print("STATUS         : ⚠️ ACCIDENT DETECTED!")
        print("ACTION         : Emergency Alert Triggered")
    else:
        print("STATUS         : ✅ Normal Driving")

def main():
    print("🚗 Digital Twin Accident Detection System Started")
    print("Press CTRL + C to stop\n")

    try:
        while True:
            acc, tilt, hr = generate_sensor_data()
            accident = detect_accident(acc, tilt)
            digital_twin_display(acc, tilt, hr, accident)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n\n🛑 System Stopped Safely")

# Run program
if __name__ == "__main__":
    main()