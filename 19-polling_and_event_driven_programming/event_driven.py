""" A Brief Study in Handling Life Events """

import asyncio

async def alarm():
    print("Wake Up!")
    print("Calling the Pizza Company.\n")
    loop.call_later(1, lambda: asyncio.create_task(alarm()))  # schedule next alarm

async def doorbell():
    print("Ding Dong!")
    await asyncio.sleep(3)  # simulate opening the door
    print('Opening the door... "Thanks for bringing the pizza!"\n')
    loop.stop()  # stop the event loop after pizza arrives

async def phonecall():
    print("Ring Ring!")
    print('Answering the phone... "Hello! Who is this?"\n')

loop = asyncio.get_event_loop()

# Schedule events
loop.call_later(1, lambda: asyncio.create_task(alarm()))
loop.call_later(4, lambda: asyncio.create_task(doorbell()))
loop.call_later(5, lambda: asyncio.create_task(phonecall()))

print("Starting the event loop...\n")
loop.run_forever()
print("The event loop stopped; closing it down.")
loop.close()