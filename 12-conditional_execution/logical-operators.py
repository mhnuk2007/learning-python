""" logical-operators.py """

def access_control(age, has_id):
    if age >= 18 and has_id:
        print("Access granted")
    else:
        print("Access denied")


def weather_advice(is_raining, is_cold):
    if is_raining or is_cold:
        print("Take a jacket")
    else:
        print("Light clothing is fine")


def login(username, password):
    if not username or not password:
        print("Username and password required")
    else:
        print("Credentials submitted")


def range_check(number):
    if 10 < number < 20:
        print("Number is between 10 and 20")
    else:
        print("Number is outside range")


if __name__ == "__main__":
    access_control(20, True)
    access_control(17, True)

    weather_advice(True, False)

    login("", "1234")
    login("admin", "1234")

    range_check(15)