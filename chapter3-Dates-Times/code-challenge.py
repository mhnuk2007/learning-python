import calendar

def count_days(year, month, whichday):
    """
    Count the number of times a specific weekday occurs in a given month.

    Parameters:
    year (int): Four-digit year (e.g., 2025)
    month (int): Month as a number (1-12)
    whichday (int): Weekday number (0=Monday, 6=Sunday)

    Returns:
    int: Number of instances of the given weekday in the month
    """
    # Get the month calendar as a list of weeks (each week is a list of 7 numbers)
    monthmatrix = calendar.monthcalendar(year, month)
    
    dayscount = 0  # Initialize counter

    # Loop over each week
    for week in monthmatrix:
        # If the weekday exists in this week (not zero), count it
        if week[whichday] != 0:
            dayscount += 1

    return dayscount

# Example usage
testyear = 2025
testmonth = 12
testday = 0  # 0 = Monday

result = count_days(testyear, testmonth, testday)
print(f"Number of Mondays in {testmonth}/{testyear}: {result}")