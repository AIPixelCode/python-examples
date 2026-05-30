# The smallest multiple

---
## Question:

___Two positive integers a, b are given as inputs. 
The goal is to find the smallest multiple of b 
such that when it is divided by a, 
the remainder lies in [0,a/2].___

---

## Example:

__a = 8__

__b = 7__

__[0, a/2] = [0, 4]__

>- 1 * 7 = 7 >> 7 mod 8 = 7 >> not in [0,4]
>- 2 * 7 = 14 >> 14 mod 8 = 6 >> not in [0,4]
>- 3 * 7 = 21 >> 21 mod 8 = 5 >> not in [0,4]
>- 4 * 7 = 28 >> 28 mod 8 = 4 >> in [0,4]

___Output: 28___

---

## Python code:

```python
a, b = map(int, input('a, b: ').split())
t = 0
r = b % a
while r > (a / 2):
    t += 1
    r = (t * b) % a
print('Output: ', t * b)
```
---

#### Written by: ___AiPixelCode___