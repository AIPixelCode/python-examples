# Alternating Group Sum Calculator

## Description

This program calculates a custom value for a list of integers by grouping the elements, computing the sum of each group, and then applying an alternating addition and subtraction pattern to the group sums.

The size of each group is specified by the user. If the final group contains fewer elements than the specified size, it is processed normally.

## How It Works

The function first divides the input list into consecutive groups of size `m`.

It then calculates the sum of each group, producing a new list of group sums.

Finally, the function computes the result by adding the sums at even positions and subtracting the sums at odd positions:

```text
group₁ − group₂ + group₃ − group₄ + ...
```

The final value is returned as an integer.

## Example

For the following input:

```text
n = 8
m = 1

List:
[1, 2, 3, 4, 5, 6, 7, 8]
```

The groups are:

```text
[1] [2] [3] [4] [5] [6] [7] [8]
```

Their sums are:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

Applying the alternating pattern gives:

```text
1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 = -4
```

Therefore, the function returns:

```text
-4
```

## Code

```python
def calculator(n: int, m: int, ls: list[int]) -> int:
    groups = [ls[i:i + m] for i in range(0, n, m)]
    sum_of_groups = list(map(sum, groups))
    evens = sum(sum_of_groups[::2])
    odds = sum(sum_of_groups[1::2])
    return evens - odds
```

---

**Author:** AiPixelCode
