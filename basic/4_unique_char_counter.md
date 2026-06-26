# Unique Character Counter

## Description

This program implements a function that finds the string with the highest number of distinct characters in a list of strings.

The function examines each string, counts its unique characters, and returns a descriptive message containing the selected string and its distinct character count.

## How It Works

The function iterates through all strings in the input list.

For each string, it converts the characters into a `set`, which automatically removes duplicates. The length of the resulting set represents the number of distinct characters in that string.

While iterating, the function keeps track of the highest distinct character count found so far and the corresponding string. After processing all strings, it returns the result as a formatted string.

## Example

For the following input:

```text
['apple', 'banana', 'cherry', 'date']
```

The distinct character counts are:

```text
apple  → 4
banana → 3
cherry → 5
date   → 4
```

Therefore, the function returns:

```text
The string "cherry" has 5 distinct characters.
```

## Code

```python
def find_most_distinct_string(strings):
    max_ucc = -1
    best_str = ""

    for s in strings:
        unique_chars = len(set(s))
        if unique_chars > max_ucc:
            max_ucc = unique_chars
            best_str = s

    return f'The string "{best_str}" has {max_ucc} distinct characters.'
```

---

**Author:** AiPixelCode
