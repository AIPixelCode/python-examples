# Combination Function

## Description

This program implements a function for calculating the binomial coefficient, commonly known as a combination.

The function returns the number of ways to choose `k` items from a set of `n` items without considering the order of selection.

## How It Works

Instead of computing factorials directly, the function uses an iterative multiplicative approach to calculate the result efficiently.

To reduce the number of iterations, it takes advantage of the symmetry property of combinations:

```text
C(n, k) = C(n, n - k)
```

The function also handles invalid cases by returning `0` when `k` is negative or greater than `n`.

## Example

For `n = 5` and `k = 3`:

```text
C(5, 3) = 10
```

This means there are 10 different ways to choose 3 items from a set of 5 items.

## Code

```python
def comb(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(min(k, n - k)):
        result = result * (n - i) // (i + 1)
    return result
```

---

**Author:** AiPixelCode
