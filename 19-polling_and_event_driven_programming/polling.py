""" Polling for Pizza Because I'm Hungry! """

import time
from pathlib import Path

hungry = True  # I need a pizza!
front_door_file = Path("front_door.txt")

while hungry:
    print("Opening the front door...")
    
    # read the front door file
    if front_door_file.exists():
        with open(front_door_file, 'r', encoding='utf-8') as f:
            front_door = f.read()
        
        if 'Delivery Person' in front_door:
            print("The pizza is here!!!!!!!!!!")
            hungry = False
        else:
            print("Not yet...")
    else:
        print("Front door is empty...")

    print("Closing the front door.\n")
    time.sleep(1)  # rest for 1 second