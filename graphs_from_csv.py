import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_FILE = "accident_log.csv"

print("📂 Current working directory:")
print(os.getcwd())

# Check if CSV exists
if not os.path.exists(CSV_FILE):
    print(f"\n❌ ERROR: '{CSV_FILE}' not found")
    print("➡ Make sure you have run Module-5 at least once")
    print("➡ CSV file must be in the SAME folder as this program")
else:
    print(f"\n✅ '{CSV_FILE}' found successfully")

    # Read CSV
    data = pd.read_csv(CSV_FILE)

    print("CSV Columns:", list(data.columns))
    print("Total accident records:", len(data))

    if len(data) == 0:
        print("\n❌ No accident data available to plot")
    else:
        plt.figure()

        plt.plot(data.index, data["Acceleration"], marker='o', label="Acceleration (g)")
        plt.plot(data.index, data["Tilt"], marker='s', label="Tilt Angle (deg)")
        plt.plot(data.index, data["HeartRate"], marker='^', label="Heart Rate (BPM)")

        plt.xlabel("Accident Events")
        plt.ylabel("Sensor Values")
        plt.title("Accident Analysis from Digital Twin")
        plt.legend()
        plt.grid(True)

        plt.show()
        plt.plot(data.index, data["tilit"],marker = '0',label="TILIT")
        plt.plot(data.index, data["CLUTCH"],marker='0',label="declaration"(g))
        plt.grid(True)
        print("\n ❌ NO accident data is available to plot")
        print("The data gained")
        print("The accident data is gained")
        println("")
        
    

