# Smallest Multiple (Modular Condition)

## 📌 Problem Statement

Given two positive integers `a` and `b`, the goal is to find the smallest multiple of `b` such that when it is divided by `a`, the remainder lies within the interval:

```
[0, a/2]
```

In other words, we search for the smallest value of `k * b` such that:

```
(k * b) % a ≤ a / 2
```

---

## 💡 Idea

We generate multiples of `b` incrementally and check their remainder when divided by `a`.
The first value that satisfies the condition is returned as the answer.

---

## ⚙️ Algorithm

1. Start with `k = 1`
2. Compute `remainder = (k * b) % a`
3. While `remainder > a / 2`, increment `k`
4. Return `k * b`

---

## 🧪 Example

### Input

```
a = 8
b = 7
```

### Allowed remainder range

```
[0, 4]
```

### Step-by-step

```
1 × 7 = 7   → 7 % 8 = 7   (not valid)
2 × 7 = 14  → 14 % 8 = 6  (not valid)
3 × 7 = 21  → 21 % 8 = 5  (not valid)
4 × 7 = 28  → 28 % 8 = 4  (valid)
```

### Output

```
28
```

---

## 🧾 Implementation (Python)

```python
a, b = map(int, input().split())

k = 1

while (k * b) % a > a / 2:
    k += 1

print(k * b)
```

---

## 📊 Complexity

* Time Complexity: `O(k)` (depends on first valid solution)
* Space Complexity: `O(1)`

---

## 👤 Author

**AiPixelCode**
