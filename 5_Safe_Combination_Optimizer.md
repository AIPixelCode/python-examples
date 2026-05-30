# Safe combination optimizer

---
## Question:
___You have a safe with k rotating locks. 
Each lock contains a sequence of nine digits (1-9) arranged in a specific order,
with a pointer initially indicating the first digit. 
Rotating a lock (clockwise or counter-clockwise) moves the pointer to adjacent digits.
Given the k-digit security code and the initial configuration of each lock,
calculate the minimum total number of rotations required to align all locks
to the target code.___

___Input:___

- The first line contains an integer k, representing the number of locks.
- The second line contains the k-digit target code. 
- Each of the next k lines contains the 9-digit sequence for a specific lock,
where the first digit is the one currently indicated by the pointer.

___Output:___
- Print the minimum total number of rotations required to set all locks to the
corresponding digits of the target code.

---
## Python code:
```python
def min_rotations(k,code,dials):
    ans=0
    for i in range(k):
        moves=dials[i].find(code[i])
        ans+=min(moves, 9-moves)
    return f"The minimum number of moves is {ans}."
```

---
## Test:
- k = 3
- code = 123
- dials = [ '241356789', '987546231', '956874231' ]
```python
ls=['241356789','987546231','956874231']
print(min_rotations(3,'123', ls))
# Output: The minimum number of moves is 7.
```

---
#### Written by: ___AiPixelCode___