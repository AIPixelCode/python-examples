# Smallest Multiple Satisfying a Modular Condition

## Description

This program finds the smallest multiple of `b` whose remainder when divided by `a` is less than or equal to half of `a`.

In other words, it searches for the smallest value of `k × b` that satisfies the following condition:

```text
(k × b) % a ≤ a / 2
```

## How It Works

The program starts with the first multiple of `b` and checks whether the condition is satisfied. If not, it continues to the next multiple and repeats the process until a valid value is found.

## Example

For `a = 8` and `b = 7`:

```text
7 % 8 = 7
14 % 8 = 6
21 % 8 = 5
28 % 8 = 4
```

Since `4 ≤ 4`, the first valid multiple is:

```text
28
```

## Code

```python
a, b = map(int, input().split())

k = 1
while (k * b) % a > a / 2:
    k += 1

print(k * b)
```

---

**Author:** AiPixelCode
