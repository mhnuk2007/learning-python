# ------------------------------------------------------------
# Date and Time Formatting in Python using datetime.strftime
# ------------------------------------------------------------

from datetime import datetime

# Get the current date and time
now = datetime.now()

# -------------------- DATE FORMATTING --------------------
# strftime() converts a datetime object into a formatted string
# Common format codes:
# %Y - Full year with century (2026)
# %y - Short year (26)
# %A - Full weekday name (Monday)
# %a - Abbreviated weekday name (Mon)
# %B - Full month name (February)
# %b - Abbreviated month name (Feb)
# %d - Day of the month (01–31)

print("The current year is:", now.strftime("%Y"))
print("Formatted date:", now.strftime("%a, %d %B, %y"))

# Locale-based formatting (depends on system language/region)
# %c - Full locale date and time
# %x - Locale date only
# %X - Locale time only
print("Locale date and time:", now.strftime("%c"))
print("Locale date only:", now.strftime("%x"))
print("Locale time only:", now.strftime("%X"))

# -------------------- TIME FORMATTING --------------------
# %H - 24-hour format (00–23)
# %I - 12-hour format (01–12)
# %M - Minutes (00–59)
# %S - Seconds (00–59)
# %p - AM / PM indicator

print("Current time (12-hour):", now.strftime("%I:%M:%S %p"))
print("Current time (24-hour):", now.strftime("%H:%M"))

# -------------------- EXTRA USEFUL FORMATS --------------------
# ISO-like date format (commonly used in APIs and databases)
print("ISO date:", now.strftime("%Y-%m-%d"))

# File-safe timestamp (useful for filenames/logs)
print("Timestamp for file:", now.strftime("%Y%m%d_%H%M%S"))