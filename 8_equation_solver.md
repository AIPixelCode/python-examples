# Equation Solver

## Description

This program reconstructs incomplete addition equations in which part of one number has been replaced with the `#` character.

The equation follows the format:

```text
a + b = c
```

Exactly one of the three numbers contains a missing section represented by one or more consecutive `#` characters. The program determines the correct digits needed to replace the missing part and verifies whether the resulting equation is mathematically valid.

If no valid replacement exists, the equation is considered unsolvable.

## How It Works

The program first identifies which part of the equation contains the missing digits.

Using the known values, it calculates the expected value of the incomplete number:

* If the first addend is incomplete, it computes `c - b`.
* If the second addend is incomplete, it computes `c - a`.
* If the result is incomplete, it computes `a + b`.

The calculated value is then compared against the original pattern containing `#` characters. A regular expression is used to verify that the calculated number matches the known digits and the positions of the missing digits.

If the pattern matches, the completed equation is returned. Otherwise, the program returns `-1`.

## Example

```text
Input:
10# + 50 = 10052

Output:
10002 + 50 = 10052
```

```text
Input:
15 + 1#2 = 136

Output:
-1
```

## Source Code

**File:** `8_equation_solver.py`

---

**Author:** AiPixelCode
