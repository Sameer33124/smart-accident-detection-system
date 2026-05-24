import random
import time
import math

ACCIDENT_THRESHOLD = 3.0  # g-force

print("Digital Twin Accident Detection Started...\n")

while True:
    ax = random.uniform(-1, 1)
    ay = random.uniform(-1, 1)
    az = random.uniform(8.5, 10.5)

    magnitude = math.sqrt(ax**2 + ay**2 + az**2)

    print(f"Ax:{ax:.2f}g Ay:{ay:.2f}g Az:{az:.2f}g | Magnitude:{magnitude:.2f}g", end=" ")

    if magnitude > ACCIDENT_THRESHOLD:
        print("🚨 ACCIDENT DETECTED!")
    else:
        print("Status: NORMAL")

    time.sleep(1)