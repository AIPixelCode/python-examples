# Equation solver

---
## Description:
___This code reconstructs a mathematical equation in the general 
form a + b = c where one of the components (either an addend or the sum) 
is incomplete. In the given equation, a part of exactly one number 
has been replaced with the # character. 
The goal is to determine the correct digits to substitute for # 
so that the equation becomes valid.___

### Rules and Constraints
- Non-negative integers: All numbers in the equation (a, b, c) 
must be non-negative integers.
- Location of the unknown part: The # character represents one or more 
consecutive missing digits from only one of the three numbers in the equation.
- Validity check: If there is no possible replacement for # 
that makes the equation correct, it means the original equation is invalid.

### Function Signature
- Function name: solve(equation)
- Input: A string containing an equation in the form a+b=c, where 
exactly one of the numbers contains the # character.
- Output: The completed equation string if a solution exists; otherwise, returns '-1'.


---
## Python code:

> **File name:** 8_equation_solver.py

---
## Test:
```python
print(solve("10# + 50 = 10052")) # 10002 + 50 = 10052
print(solve("15 + 1#2 = 136"))   # -1
```

---
#### Written by: ___AiPixelCode___