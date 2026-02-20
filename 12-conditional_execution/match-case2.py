def weekend_or_weekday(day: str):
    match day.capitalize():
        case 'Saturday' | 'Sunday':
            return "Weekend special!"
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return "Weekday special!"
        case _:
            return "Invalid day"