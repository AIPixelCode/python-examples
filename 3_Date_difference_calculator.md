# Date difference calculator

---
## Question:
___Write a function named "day_calculator" that takes
a date string in the format "YYYY-MM-DD" as input.
The function should compare this date with the current date
and return a string describing the difference in days:___
- ___If the date is in the past, return: "{x} days ago."___
- ___If the date is in the future, return: "{x} days later."___
- ___If the days is today, return: "It's today."___
> **note:** Use datetime library

---
## Example:
- __Today: 2026-05-25__
- __input string: '2026-05-2'__
>___Output: 23 days ago.___

---

## Python code:
```python
from datetime import datetime as dt

def day_calculator(date_str):
    d = dt.strptime(date_str, '%Y-%m-%d').date()
    now = dt.now().date() # 2026-05-25
    diff_date = (now - d).days
    if diff_date < 0:
        return f'{abs(diff_date)} days later.'
    elif diff_date == 0:
        return "It's today."
    else:
        return f'{diff_date} days ago.'
```

---
## Tests:
```python
print(day_calculator('2026-05-2')) # 23 days ago.
print(day_calculator('2026-05-27')) # 2 days later.
print(day_calculator('2026-05-25')) # It's today.
```

---
#### Written by: ___AiPixelCode___