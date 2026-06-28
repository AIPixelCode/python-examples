# Real Number Format Validator

## Description

This program validates whether a collection of strings represents correctly formatted real numbers.

Each input string is checked against a set of formatting rules, including optional signs, decimal notation, scientific notation, and surrounding whitespace. For every string, the program reports whether its format is valid.

## How It Works

The function processes each string independently using a regular expression.

A number is considered valid if it satisfies the following conditions:

* It may begin with an optional `+` or `-` sign.
* It contains at least one digit.
* It may include a decimal point, provided that digits exist on both sides of the point.
* It may include an exponent introduced by `e` or `E`, optionally followed by a sign and one or more digits.
* Leading and trailing whitespace is allowed, but whitespace is not permitted inside the number itself.

For every input string, the function returns:

* `LEGAL` if the string matches the required format.
* `ILLEGAL` otherwise.

## Example

Given the following input:

```text
['1.5e+2', '3.', '1.1.1', '1+e5', ' -123.45 ', '0', '+10E-5', 'abc', '1. ', '.5', '5e', '5e1.0']
```

The function returns:

```text
['LEGAL', 'ILLEGAL', 'ILLEGAL', 'ILLEGAL', 'LEGAL', 'LEGAL', 'LEGAL', 'ILLEGAL', 'ILLEGAL', 'ILLEGAL', 'ILLEGAL', 'ILLEGAL']
```

## Code

```python
import re
def real_numbers(numbers: list[str]):
    result = []
    for number in numbers:
        if re.match(r'^\s*[+-]?(\d+(\.\d+)?)([eE][+-]?\d+)?\s*$', number):
            result.append('LEGAL')
        else:
            result.append('ILLEGAL')
    return result
```

---

**Author:** AiPixelCode
