# Combination function

---
## Question:
___The goal is implement the function "comb". 
This function takes two integer n and k as input 
and return the value of the combination 
"k choose n" as its output.___

>_comb(n,k) = n! / (k! * (n-k)!)_

---
## Example:
__n = 5__

__k = 3__

_comb(5,3) = 5! / (3! * (5-3)!) = 10_

>___Output: 10___

---

## Python code:

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

#### Written by: ___AiPixelCode___