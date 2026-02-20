""" Polling Example - Checking a Simulated Sensor """

import random
import time

sensor_active = False

print("Monitoring sensor...")

for _ in range(10):
    sensor_active = random.choice([True, False])
    if sensor_active:
        print("Sensor triggered!")
    else:
        print("Sensor inactive...")
    time.sleep(1)