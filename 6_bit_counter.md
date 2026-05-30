# Bit counter

---
## Question:
___Write a Python program that takes an integer as input and calculates the 
total number of set bits (bits with a value of 1) in its binary representation. 
The program should then output the final count.___

---
## Python code:
```python
def count_bits(n):
    bit_1 = f"{n:b}".count('1')
    return f"Total number of set bits(1): {bit_1}"
```

---
## Test:
- n = 37
- binary(n) = 100101

```python
print(count_bits(37))
# Output: Total number of set bits(1): 3
```

---
#### Written by: ___AiPixelCode___