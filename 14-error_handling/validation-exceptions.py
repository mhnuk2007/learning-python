""" validation-exceptions.py - Raising Exceptions for Validation """

def check_temperature(temp):
    if temp < -50 or temp > 50:
        raise ValueError(f"Temperature {temp}°C is unrealistic.")
    print(f"Temperature {temp}°C is within normal range.")


if __name__ == "__main__":
    for t in [20, -100, 30]:
        try:
            check_temperature(t)
        except ValueError as e:
            print("Validation error:", e)