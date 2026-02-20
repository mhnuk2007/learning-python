""" Event-Driven Example - Async Sensor Monitoring """

import asyncio
import random

async def sensor_monitor():
    for i in range(10):
        await asyncio.sleep(1)
        if random.choice([True, False]):
            print(f"Sensor triggered at iteration {i}")
        else:
            print(f"No event at iteration {i}")

asyncio.run(sensor_monitor())