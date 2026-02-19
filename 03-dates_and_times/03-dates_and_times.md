# 03-dates_and_times

## Learning goals

- Work with `datetime`, `date`, and `timedelta`.
- Format date/time values for output.
- Use `calendar` utilities for month/year views.

## Key definitions

- `datetime`: combined date and time object.
- `timedelta`: duration for arithmetic on dates/times.
- `strftime`: formatting method for date/time strings.

## Core concepts

- `datetime.now()` gives current local date and time.
- `timedelta` supports add/subtract operations.
- `strftime` converts datetime objects to readable text.
- `calendar` helps calculate weekday/month structures.

## Common mistakes

- Mixing string dates with datetime objects without parsing.
- Ignoring timezone differences in real applications.

## Quick recap

- Use objects, not plain strings, for date arithmetic.
- Format only at display boundaries.
