# Name Frequency Counter

## Description

This program counts how many times each first name appears in a list of people and determines the highest occurrence among all names.

Each input consists of a first name and a last name, but only the first name is considered when calculating the frequency.

## How It Works

The program reads each person's first and last name and stores the occurrence count of every first name in a dictionary.

For each new entry, the corresponding counter is updated using the dictionary's `get()` method.

After processing all records, the program finds and prints the largest value in the dictionary, representing the maximum number of times a first name appears.

## Example

For the following input:

```text
6
Robert Wilson
Mary Moore
Robert Taylor
Mary Anderson
Robert Thomas
James Jackson
```

The first-name frequencies are:

```text
Robert → 3
Mary   → 2
James  → 1
```

Therefore, the program prints:

```text
3
```

## Code

```python
names = dict()

cnt = int(input())

for i in range(cnt):
    name, family = input().split()
    names[name] = names.get(name, 0) + 1

print(max(names.values()))
```

---

**Author:** AiPixelCode
