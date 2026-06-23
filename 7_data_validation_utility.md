# Data Validation Utility

## Description

This program provides two utility functions for validating email addresses and mobile phone numbers using regular expressions.

The functions check whether the provided input matches predefined patterns and return a boolean result indicating whether the format is valid.

## How It Works

### Email Validation

The `validate_email()` function verifies that an email address follows a specific format:

```text
username@domain.tld
```

The validation rules are:

* The username may contain letters, numbers, dots (`.`), and underscores (`_`).
* The domain may contain only letters and numbers.
* The top-level domain (TLD) must consist of exactly three letters.

### Phone Number Validation

The `validate_phone()` function validates mobile phone numbers in three supported formats:

```text
09123456789
+989123456789
00989123456789
```

The validation pattern ensures that all accepted numbers represent the same mobile number structure while allowing different local and international prefixes.

## Example

```text
validate_email("sample@school.edu")  → True
validate_email("invalid@invalid")    → False

validate_phone("09215546321")        → True
validate_phone("093311111111")       → False
```

## Code

```python
import re

def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$", email))

def validate_phone(number):
    return bool(re.match(r"^(0|\+98|0098)9[0-9]{9}$", number))
```

---

**Author:** AiPixelCode
