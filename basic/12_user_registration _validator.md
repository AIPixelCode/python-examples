# User Registration Validator

## Description

This program validates user registration information based on a predefined set of username and password rules.

The function receives multiple username–password pairs as keyword arguments and returns a list containing only the usernames that satisfy all validation requirements.

## How It Works

The function evaluates each username and password against the following rules:

* The username must contain at least 4 characters.
* The username must not appear in the list of prohibited usernames.
* The password must contain at least 6 characters.
* The password must not consist entirely of digits.

Each valid username is added to the result list, which is returned after all entries have been processed.

## Example

Given the following registration data:

```text
john_doe = "SecurePass123"
alex     = "123456"
bob      = "a1b2c3"
codecup  = "qwe456r"
```

The validation results are:

* `john_doe` ✔ Valid
* `alex` ✘ Password contains only digits.
* `bob` ✘ Username is shorter than 4 characters.
* `codecup` ✘ Username is prohibited.

Therefore, the function returns:

```text
['john_doe']
```

## Code

```python
def check_registration_rules(**kwargs: str):
    result = []
    invalid_usernames = ['codecup']

    for username, password in kwargs.items():
        if len(username) >= 4 and username not in invalid_usernames:
            if len(password) >= 6 and not password.isdigit():
                result.append(username)

    return result
```

---

**Author:** AiPixelCode
