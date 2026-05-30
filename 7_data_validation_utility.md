# Data validation utility

---
## Description:
___This code is used to validate the correct format of
emails and mobile phone numbers. Its purpose is to ensure
that the data entered by the user follows standard patterns.___

1. ___Email Validation (validate_email)___

This function checks if the input email strictly follows the 
username@domain.tld pattern. The applied rules are:
- Username: Can include English letters, numbers, dots (.), and underscores (_).
- Domain: Must consist only of English letters and numbers.
- TLD (Top-Level Domain): Must be exactly 3 English letters (e.g., com or net).

2. ___Phone Number Validation (validate_phone)___

This function identifies and validates mobile numbers in the 
following three standard formats:

- Local Format: 11 digits starting with 09 (e.g., 09123456789).
- International (+) Format: 13 characters starting with +989 (e.g., +989123456789).
- International (00) Format: 14 digits starting with 00989 (e.g., 00989123456789).

> **Output:** Both functions return True if the format is correct, and False otherwise.

---
## Python code:
```python
import re

def validate_email(email):
    return bool(re.match(r"^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$", email))

def validate_phone(number):
    return bool(re.match(r"^(0|\+98|0098)9[0-9]{9}$", number))
```

---
## Test:
```python
print(validate_email('sample@school.edu'))  # True
print(validate_email('invalid@invalid'))    # False
print(validate_phone('09215546321'))        # True
print(validate_phone('093311111111'))       # False
```

---
#### Written by: ___AiPixelCode___