# Safe Combination Optimizer

## Description

This program calculates the minimum number of rotations required to align a set of circular locks with a target security code.

Each lock contains a circular sequence of nine digits, and the pointer initially indicates the first digit in the sequence. The goal is to rotate each lock until the required digit from the target code is aligned with the pointer while minimizing the total number of moves.

## How It Works

The function processes each lock independently.

For every position in the target code:

1. It finds the location of the required digit within the corresponding lock sequence.
2. It calculates the number of clockwise rotations needed to reach that digit.
3. Since the lock is circular, rotating in the opposite direction may require fewer moves.
4. The function selects the smaller of the two possible rotation counts and adds it to the total.

After all locks have been processed, the function returns the minimum total number of rotations.

## Example

Given the following configuration:

```text
Target code: 123

Lock 1: 241356789
Lock 2: 987546231
Lock 3: 956874231
```

The function determines the minimum rotations required for each lock and returns:

```text
The minimum number of moves is 7.
```

## Code

```python
def min_rotations(k, code, dials):
    ans = 0

    for i in range(k):
        moves = dials[i].find(code[i])
        ans += min(moves, 9 - moves)

    return f"The minimum number of moves is {ans}."
```

---

**Author:** AiPixelCode
