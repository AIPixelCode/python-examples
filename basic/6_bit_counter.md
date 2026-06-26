# Bit Counter

## Description

This program counts the number of set bits in the binary representation of an integer.

A set bit is a bit with the value `1`. The function converts the input number to binary form and determines how many `1` bits it contains.

## How It Works

The function first converts the input integer into its binary representation using Python's binary formatting syntax.

It then counts the occurrences of the character `'1'` in the resulting binary string. The final count represents the total number of set bits in the number.

## Example

For the integer:

```text
37
```

Its binary representation is:

```text
100101
```

Since the binary value contains three `1` bits, the function returns:

```text
Total number of set bits (1): 3
```

## Code

```python
def count_bits(n):
    bit_1 = f"{n:b}".count('1')
    return f"Total number of set bits(1): {bit_1}"
```

---

**Author:** AiPixelCode
