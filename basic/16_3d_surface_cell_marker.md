# 3D Surface Cell Marker

## Description

This program identifies the surface cells of a three-dimensional grid and marks them by modifying the original data structure.

Every cell located on the outer boundary of the grid is assigned the value `1`, while all interior cells are assigned the value `0`. The function updates the input grid directly without creating a new one.

## How It Works

The function first determines the dimensions of the three-dimensional grid.

It then iterates through every cell using three nested loops. For each position, it checks whether the cell lies on any outer boundary:

* The first or last layer.
* The first or last row.
* The first or last column.

If any of these conditions is true, the cell is considered part of the surface and its value is set to `1`. Otherwise, the cell is an interior element and its value is set to `0`.

Because the function modifies the original grid, it does not return any value.

## Example

Given the following `3 × 3 × 3` grid:

```text
All cells initially contain the value 5.
```

After applying the function, the grid becomes:

```text
Layer 1:
1 1 1
1 1 1
1 1 1

Layer 2:
1 1 1
1 0 1
1 1 1

Layer 3:
1 1 1
1 1 1
1 1 1
```

Only the center cell remains `0` because it is completely surrounded by other cells.

## Code

```python
def coloring(ls):
    x, y, z = map(len, [ls, ls[0], ls[0][0]])
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (
                    i == 0 or i == x - 1 or
                    j == 0 or j == y - 1 or
                    k == 0 or k == z - 1
                ):
                    ls[i][j][k] = 1
                else:
                    ls[i][j][k] = 0
```

---

**Author:** AiPixelCode
