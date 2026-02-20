""" raising-exceptions.py """

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount


if __name__ == "__main__":
    try:
        new_balance = withdraw(100, 150)
        print("New balance:", new_balance)
    except ValueError as e:
        print("Error:", e)