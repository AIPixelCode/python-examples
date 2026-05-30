# Unique char counter

---
## Question:
___Define a function named "find_most_distinct_string" that accepts a list of strings as input.
The function should identify the string with the highest number of unique
(distinct) characters and return a string containing both the identified
string and its character count.___

---
## Example:
- __Input list: [ 'aabc', 'xyz', 'hello' ]__
>___Output: The string "hello" has 4 distinct characters.___

---

## Python code:
```python
def find_most_distinct_string(strings):
    max_ucc = -1
    best_str = ""
    for s in strings:
        unique_chars = len(set(s))
        if unique_chars > max_ucc:
            max_ucc = unique_chars
            best_str = s
    return f'The string "{best_str}" has {max_ucc} distinct characters"'
```

---
## Test:
```python
ls = ['apple', 'banana', 'cherry', 'date']
print(find_most_distinct_string(ls))
# Output: The string "cherry" has 5 distinct characters.
```

---
#### Written by: ___AiPixelCode___