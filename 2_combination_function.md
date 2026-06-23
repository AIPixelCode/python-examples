# Combination Function

## Description

This program implements a function comb(n, k) that computes the binomial coefficient:

```
C(n, k) = n! / (k! * (n - k)!)
```

---

## Idea

We compute the combination efficiently without calculating full factorials, using an iterative multiplicative approach.

---

## Example

**Input:**

```
n = 5, k = 3
```

**Process:**

```
C(5,3) = 5! / (3! * 2!) = 10
```

**Output:**

```
10
```

---

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

#### Author: AiPixelCode
