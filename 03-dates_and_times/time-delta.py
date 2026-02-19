from datetime import datetime, timedelta

# Create and display a basic timedelta object
# This represents a duration of 5 days, 3 hours, and 30 minutes
print("Basic timedelta:", timedelta(days=5, hours=3, minutes=30))

# Get the current date and time
today = datetime.now()
print("Today's date:", today)

# Add 365 days to the current date (approx. one year ahead)
print("One year from now, it will be:", today + timedelta(days=365))

# Add 1 week and 3 days to the current date
print("In one week and three days, it will be:", today + timedelta(weeks=1, days=3))

# Subtract 1 week from the current date
one_week_ago = today - timedelta(weeks=1)

# Format the past date into a readable string
# %A = weekday name, %B = month name, %d = day, %Y = year
formatted_date = one_week_ago.strftime("%A %B %d, %Y")
print("One week ago, it was:", formatted_date)

# ---------------- Birthday Countdown Example ----------------

# Set next birthday date for the current year (July 14)
nbd = datetime(today.year, 7, 14)

# If the birthday already passed this year,
# move it to the next year
if nbd < today:
    nbd = datetime(today.year + 1, 7, 14)

# Calculate the difference between next birthday and today
# .days extracts only the number of days from the timedelta
days_until_birthday = (nbd - today).days

print("Days until my next birthday:", days_until_birthday)

# Formatting as local date and time string
print("Next birthday (local format):", nbd.strftime("%c"))
print("Next birthday (local date):", nbd.strftime("%x"))
print("Next birthday (local time):", nbd.strftime("%X"))

# Time formatting
# %I/%H = hour (12-hour/24-hour clock), %M = minute, %S = second, %p = AM/PM
print("Time now:", today.strftime("%I:%M:%S %p"))
print("Time now (24-hour format):", today.strftime("%H:%M:%S"))
