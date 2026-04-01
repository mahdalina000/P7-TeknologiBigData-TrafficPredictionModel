import json
import time
import random
import os
from datetime import datetime

# Path folder untuk data streaming transportation
OUTPUT_PATH = "stream_data/transportation"
os.makedirs(OUTPUT_PATH, exist_ok=True)

locations = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan"]
vehicles = ["Car", "Motorbike", "Taxi", "Bus"]

print("🚀 Transportation Data Generator Started...")
print(f"📁 Saving data to: {OUTPUT_PATH}")

i = 1
while True:
    data = {
        "trip_id": f"TRIP-{i:04d}",
        "vehicle_type": random.choice(vehicles),
        "location": random.choice(locations),
        "distance": round(random.uniform(1.0, 25.0), 2),
        "fare": random.randint(15000, 150000),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    file_path = f"{OUTPUT_PATH}/trip_{i}.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
        
    print(f"✅ Generated: {data['trip_id']} | {data['location']} | Rp{data['fare']}")
    
    i += 1
    time.sleep(2) # Generate data setiap 2 detik
