""" Event-Driven Example - Keyboard Input (Asyncio) """

import asyncio

async def monitor_input():
    while True:
        user_input = await asyncio.to_thread(input, "Type something: ")
        print(f"You typed: {user_input}")
        if user_input.lower() == "exit":
            break

asyncio.run(monitor_input())