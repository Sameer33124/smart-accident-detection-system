import random
import time
import math
from datetime import datetime
import matplotlib.pyplot as plt

# -----------------------------
# Configuration
# -----------------------------
ACCIDENT_THRESHOLD = 3.0
SAMPLING_TIME = 1
MAX_POINTS = 20   # points shown on graph

# -----------------------------
# Data Storage
# -----------------------------
ax_list, ay_list, az_list, mag_list = [], [], [], []

plt.ion()  # interactive mode
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

print("\n🚗 Digital Twin – Accident Detection with Live Graphs Started\n")

while True:
    # Virtual Accelerometer
    ax_val = random.uniform(-1.0, 1.0)
    ay_val = random.uniform(-1.0, 1.0)
    az_val = random.uniform(8.5, 10.5)

    gravity = 9.8
    magnitude = math.sqrt(
        ax_val**2 + ay_val**2 + (az_val-gravity)**2
    )
    
    # Store data
    ax_list.append(ax_val)
    ay_list.append(ay_val)
    az_list.append(az_val)
    mag_list.append(magnitude)

    if len(ax_list) > MAX_POINTS:
        ax_list.pop(0)
        ay_list.pop(0)
        az_list.pop(0)
        mag_list.pop(0)

    # Console Output
    print(f"Ax:{ax_val:.2f} Ay:{ay_val:.2f} Az:{az_val:.2f} | Mag:{magnitude:.2f}", end=" ")

    # Accident Detection
    if magnitude > ACCIDENT_THRESHOLD:
        print("🚨 ACCIDENT DETECTED!")
        print("📍 Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        break
    else:
        print("Status: NORMAL")

    # -----------------------------
    # Plotting
    # -----------------------------
    ax[0].cla()
    ax[0].plot(ax_list, label="Ax")
    ax[0].plot(ay_list, label="Ay")
    ax[0].plot(az_list, label="Az")
    ax[0].set_title("Accelerometer Axes")
    ax[0].legend()
    ax[0].grid()

    ax[1].cla()
    ax[1].plot(mag_list, label="Magnitude", color="red")
    ax[1].axhline(ACCIDENT_THRESHOLD, linestyle="--", label="Threshold")
    ax[1].set_title("Resultant Acceleration")
    ax[1].legend()
    ax[1].grid()

    plt.pause(0.01)
    time.sleep(SAMPLING_TIME)

plt.ioff()
plt.show()


