# Chapter 3: Dates & Times

This chapter covers working with dates, times, and calendars in Python using the `datetime` and `calendar` modules.

## Prerequisites

- Python 3.x
- Terminal access (PowerShell, CMD, or Bash)

## How to run

From the project root:

```powershell
cd chapter3-Dates-Times
python .\dates.py
```

Replace `dates.py` with any file in this chapter.

## Files and topics

| File | Focus |
| --- | --- |
| `dates.py` | Basic date/time operations: `date.today()`, `datetime.now()`, extracting date components |
| `date-time-formatting.py` | `strftime()` format codes for dates and times, locale-based formatting |
| `time-delta.py` | `timedelta` for date arithmetic, adding/subtracting time, countdown example |
| `calenders.py` | `calendar` module: yearly/monthly calendars, leap years, weekday calculations |
| `code-challenge.py` | Challenge: count occurrences of a specific weekday in a month |

## Suggested order

1. `dates.py`
2. `date-time-formatting.py`
3. `time-delta.py`
4. `calenders.py`
5. `code-challenge.py`

## Key concepts

### datetime module

```python
from datetime import date, datetime, timedelta

# Current date and time
today = date.today()
now = datetime.now()

# Date arithmetic
one_week_later = today + timedelta(weeks=1)
```

### strftime format codes

| Code | Meaning | Example |
| --- | --- | --- |
| `%Y` | Full year | 2026 |
| `%m` | Month (01-12) | 02 |
| `%d` | Day (01-31) | 18 |
| `%H` | Hour 24h (00-23) | 22 |
| `%I` | Hour 12h (01-12) | 10 |
| `%M` | Minute (00-59) | 30 |
| `%S` | Second (00-59) | 45 |
| `%A` | Weekday name | Wednesday |
| `%B` | Month name | February |
| `%p` | AM/PM | PM |

### calendar module

```python
import calendar

# Check leap year
calendar.isleap(2024)  # True

# Print month calendar
print(calendar.month(2026, 2))

# Get month calendar as matrix
calendar.monthcalendar(2026, 2)
```

## Notes

- All files in this chapter are self-contained and can be run independently.
- `time-delta.py` includes a birthday countdown example that uses July 14 as the birthday date.
- `calenders.py` outputs a lot of text (full year calendars), so the output may be lengthy.