# Divisor Generator

## Description

This program implements a generator function that produces all positive divisors of a given integer in ascending order.

Instead of storing the divisors in a list, the function yields each divisor one at a time, making it suitable for sequential iteration.

## How It Works

The function iterates through all integers from `1` to the given number.

For each value, it checks whether the number is evenly divisible by the current integer. If the remainder is zero, the integer is a divisor and is immediately yielded using Python's `yield` statement.

Because the values are generated one by one, the function returns a generator rather than a list.

## Example

For the input:

```text
15
```

The generated divisors are:

```text
1
3
5
15
```

When converted to a list, the result is:

```text
[1, 3, 5, 15]
```

## Code

```python
def divs(a: int):
    for i in range(1, a + 1):
        if a % i == 0:
            yield i
```

---

**Author:** AiPixelCode
