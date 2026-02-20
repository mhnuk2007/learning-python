""" Scrubbing A Stubborn Pan """

import random


def scrub_pan():
    scrub_count = 0

    while True:
        scrub_count += 1
        print(f"Scrubbed the pan {scrub_count} times.")

        # 20% chance of being clean
        if random.random() < 0.2:
            print("All clean!")
            break
        else:
            print("Still dirty...")

        print("Rinsing to check if the pan is clean...\n")


if __name__ == "__main__":
    scrub_pan()