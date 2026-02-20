# Example: Enhanced Exception Handling in Python
# Demonstrates handling multiple exceptions with try, except, else, and finally

x = 10  # Base number to divide

# -------------------------------
# Example 1: Basic ZeroDivisionError
# -------------------------------
try:
    print("Dividing by zero to demonstrate exception handling...")
    print(x / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero!")

print("-" * 50)

# -------------------------------
# Example 2: User input with exception handling
# -------------------------------
try:
    # Ask user for a number to divide by
    answer = input("Enter a number to divide 10 by: ")

    # Convert input to integer (may raise ValueError)
    divisor = int(answer)

    # Perform division (may raise ZeroDivisionError)
    result = x / divisor

except ValueError as ve:
    # Handles non-integer input
    print("Invalid input! Please enter a valid integer.", ve)

except ZeroDivisionError as zde:
    # Handles division by zero
    print("Cannot divide by zero!", zde)

else:
    # Executes if no exception occurs
    print(f"Success! 10 divided by {divisor} is {result}")

finally:
    # Executes no matter what
    print("Execution of try-except-finally block is complete.")

print("-" * 50)
print("Program continues running normally...")