import calendar
from datetime import datetime

# -------------------------------------------------
# Print the full calendar for the year 2026
# -------------------------------------------------
print(calendar.calendar(2026))

# -------------------------------------------------
# Print the calendar for February 2024
# (2024 is a leap year, so February has 29 days)
# -------------------------------------------------
print(calendar.month(2024, 2))

# -------------------------------------------------
# Get current year and month using datetime module
# -------------------------------------------------
current_year = datetime.now().year
current_month = datetime.now().month

print("Current Year Calendar:\n")
print(calendar.calendar(current_year))

print("Current Month Calendar:\n")
print(calendar.month(current_year, current_month))

# -------------------------------------------------
# Create a plain text calendar with Sunday as first day
# TextCalendar allows formatting customization
# -------------------------------------------------
plain_cal = calendar.TextCalendar(calendar.SUNDAY)
print("Plain Text Calendar 2025:\n")
print(plain_cal.formatyear(2025))

# -------------------------------------------------
# Check if a year is a leap year
# -------------------------------------------------
year_to_check = 2028
print(f"Is {year_to_check} a leap year? ->", calendar.isleap(year_to_check))

# -------------------------------------------------
# Count how many leap years are in a range
# -------------------------------------------------
print("Leap years between 2000 and 2030:", calendar.leapdays(2000, 2030))

# -------------------------------------------------
# Print all month and day names
# -------------------------------------------------
print("\nMonth Names:")
for month_name in calendar.month_name:
    print(month_name)

print("\nDay Names:")
for day_name in calendar.day_name:
    print(day_name)

# -------------------------------------------------
# Loop over all days of a specific month
# itermonthdays returns integers for each day slot
# 0 means the day belongs to previous/next month
# Example: August 2026
# -------------------------------------------------
print("\nDays in August 2026 (0 = overlapping month):")
for day in plain_cal.itermonthdays(2026, 8):
    print(day)

# -------------------------------------------------
# Example: Find the first Monday of each month in 2026
# -------------------------------------------------
print("\nFirst Monday of each month in 2026:")
for month in range(1, 13):
    month_matrix = calendar.monthcalendar(2026, month)

    # If Monday is in first week
    if month_matrix[0][calendar.MONDAY] != 0:
        first_monday = month_matrix[0][calendar.MONDAY]
    else:
        first_monday = month_matrix[1][calendar.MONDAY]

    print(f"{calendar.month_name[month]}: {first_monday}")