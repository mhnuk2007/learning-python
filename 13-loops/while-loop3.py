""" Putting Away Clean Dishes """

import random


def unload_dishwasher():
    dishwasher = [
        'plate', 'bowl', 'cup', 'knife', 'fork',
        'spoon', 'plate', 'spoon', 'bowl', 'cup',
        'knife', 'cup', 'cup', 'fork', 'bowl',
        'fork', 'plate', 'cup', 'spoon', 'knife'
    ]

    cabinet_capacity = random.randint(5, 20)
    print(f"\nCabinet has space for {cabinet_capacity} dishes.\n")

    stored = 0

    while dishwasher and stored < cabinet_capacity:
        dish = dishwasher.pop()
        print(f"Putting {dish} in the cabinet")
        stored += 1

    if dishwasher:
        print("\nOut of space! Remaining dishes stay in dishwasher.")
    else:
        print("\nAll dishes stored successfully!")


if __name__ == "__main__":
    unload_dishwasher()