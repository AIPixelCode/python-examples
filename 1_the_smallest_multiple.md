# Smallest Multiple (Modular Condition)

## Description

Given two integers `a` and `b`, this program finds the smallest multiple of `b` such that:

```
(k * b) % a ≤ a / 2
```

---

## Idea

We iterate over multiples of `b` and check their remainder modulo `a` until the condition is satisfied.

---

## Example

**Input:**

```id="w1k9zp"
a = 8, b = 7
```

**Process:**

```id="c3m8fd"
7 % 8 = 7   → invalid  
14 % 8 = 6  → invalid  
21 % 8 = 5  → invalid  
28 % 8 = 4  → valid
```

**Output:**

```id="x7n2aa"
28
```

---

## Code

```python id="p0k2ld"
a, b = map(int, input().split())

k = 1
while (k * b) % a > a / 2:
    k += 1

print(k * b)
```

---

#### Author: AiPixelCode
