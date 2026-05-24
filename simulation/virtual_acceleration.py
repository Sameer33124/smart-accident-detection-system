import random
import time

print("Virtual Accelerometer started ...\n")

while True:
    ax=round (random.uniform(-1.0,1.0),2)
    ay=round (random.uniform(-1.0,1.0),2)
    az=round (random.uniform(-1.0,1.0),2)

    print(f"AX :{ax} g | AY :{ay} g | AZ :{az} g")
    time.sleep(1)