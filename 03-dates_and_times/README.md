# Chapter 3: Dates & Times

This chapter covers working with dates, times, and calendars in Python using the `datetime` and `calendar` modules.

## Prerequisites

- Python 3.x
- Terminal access (PowerShell, CMD, or Bash)

## How to run

From the project root:

```powershell
cd 03-dates_and_times
python .\dates.py
```

Replace `dates.py` with any file in this chapter.

## Files and topics

| File | Focus |
| --- | --- |
| `dates.py` | Basic date/time operations: `date.today()`, `datetime.now()`, extracting date components |
| `date-time-formatting.py` | `strftime()` format codes for dates and times, locale-based formatting |
| `time-delta.py` | `timedelta` for date arithmetic, adding/subtracting time, countdown example |
| `calendars.py` | `calendar` module: yearly/monthly calendars, leap years, weekday calculations |
| `code-challenge.py` | Challenge: count occurrences of a specific weekday in a month |

## Suggested order

1. `dates.py`
2. `date-time-formatting.py`
3. `time-delta.py`
4. `calendars.py`
5. `code-challenge.py`

## Notes

- All files in this chapter are self-contained and can be run independently.
- `time-delta.py` includes a birthday countdown example.
- `calendars.py` outputs a lot of text (full year calendars), so the output may be lengthy.
