# Name Capitalizer

## Description

This program standardizes the capitalization of a list of names.

Each name is converted to title case, ensuring that the first letter of every word is uppercase while all remaining letters are lowercase. The function preserves the original order of the names and returns a new list containing the formatted results.

## How It Works

The function applies Python's built-in `title()` method to every string in the input list.

The `title()` method automatically capitalizes the first letter of each word and converts the remaining letters to lowercase.

To process all names efficiently, the function uses the `map()` function and converts the resulting iterator into a list before returning it.

## Example

For the following input:

```text
['nazaNIN ZAHRA', 'ALI KHAN']
```

The function returns:

```text
['Nazanin Zahra', 'Ali Khan']
```

## Code

```python
def capitalize(names: list[str]):
    return list(map(lambda x: x.title(), names))
```

---

**Author:** AiPixelCode
