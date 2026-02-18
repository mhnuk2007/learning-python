# This code demonstrates how to work with dates and times in Python using the datetime module.
from datetime import date, datetime

# Get today's date from the date object
today = date.today()
# Print today's date
print("Today's date:", today)

# Get the year, month, and day from today's date
print("Day:", today.day, " | Month:", today.month, " | Year:", today.year)

# Retrieve the weekday as an integer (0=Monday, 6=Sunday)
print("Weekday (0=Monday, 6=Sunday):", today.weekday())

# Convert the weekday integer to a human-readable format
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Day of the week:", weekdays[today.weekday()])

# Get today's date from datetime object
now = datetime.now()
print("Current date and time:", now)

# Get the year, month, day, hour, minute, and second from the datetime object
print("Year:", now.year, " | Month:", now.month, " | Day:", now.day, " | Hour:", now.hour, " | Minute:", now.minute, " | Second:", now.second)

# Get the current time in a specific format
print("Current time:", now.time())


