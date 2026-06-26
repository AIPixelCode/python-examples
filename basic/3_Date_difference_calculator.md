# Date Difference Calculator

## Description

This program implements a function that compares a given date with the current date and returns a human-readable description of the difference in days.

Depending on the result, the function indicates whether the date is in the past, in the future, or exactly today.

## How It Works

The function receives a date string in the `YYYY-MM-DD` format and converts it into a date object using Python's `datetime` module.

It then calculates the difference between the current date and the provided date:

* If the date is in the past, it returns the number of days ago.
* If the date is in the future, it returns the number of days later.
* If both dates are the same, it returns `"It's today."`

## Example

Assume today's date is `2026-05-25`.

```text
Input:  2026-05-02
Output: 23 days ago.

Input:  2026-05-27
Output: 2 days later.

Input:  2026-05-25
Output: It's today.
```

## Code

```python
from datetime import datetime as dt

def day_calculator(date_str):
    d = dt.strptime(date_str, '%Y-%m-%d').date()
    now = dt.now().date()
    diff_date = (now - d).days

    if diff_date < 0:
        return f'{abs(diff_date)} days later.'
    elif diff_date == 0:
        return "It's today."
    else:
        return f'{diff_date} days ago.'
```

---

**Author:** AiPixelCode
