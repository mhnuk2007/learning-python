""" I'll Have the Special! """

def order_special(day: str):
    # Normalize input (capitalize first letter)
    day = day.capitalize()

    match day:
        case 'Sunday':
            return 'spinach pizza'
        case 'Monday':
            return 'mushroom pizza'
        case 'Tuesday':
            return 'pepperoni pizza'
        case 'Wednesday':
            return 'veggie pizza'
        case 'Thursday':
            return 'bbq chicken pizza'
        case _:
            return None


if __name__ == "__main__":
    today = 'Christmas'
    special = order_special(today)

    if special:
        print(f"\nToday is {today}, and the special is {special}.\n")
    else:
        print(f"\nThere is no special for {today}.\n")