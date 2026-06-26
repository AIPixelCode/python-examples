# Minesweeper Board Generator

## Description

This program generates a complete Minesweeper board from the positions of the mines.

Each mine is represented by the `*` symbol, while every other cell contains the number of adjacent mines in the eight surrounding positions. The completed board is then printed in a grid format.

## How It Works

The program first creates a two-dimensional grid with an additional border of empty cells. This extra border simplifies neighbor checking by eliminating the need for boundary-condition tests.

After reading the mine locations, the program places a `*` in each corresponding cell.

It then visits every non-mine cell and examines its eight neighboring positions. For each neighboring mine found, the cell's counter is incremented.

Finally, the completed Minesweeper board is printed, displaying either a mine (`*`) or the number of adjacent mines for every cell.

## Example

For the following mine locations:

```text
Board size: 4 × 3

Mines:
(1, 1)
(1, 3)
(3, 2)
(4, 2)
(4, 3)
```

The generated board is:

```text
* 2 *
2 3 2
2 * 3
2 * *
```

## Source Code

**File:** `10_minesweeper_board_generator.py`

---

**Author:** AiPixelCode
