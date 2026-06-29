# Calculate Row Sums in a CSV File

## Description

This program reads a CSV file containing integer values and calculates the sum of each row.

For every row in the input file, the calculated sum is appended as a new column. The updated rows are then written to a new file named `result.csv`.

The implementation uses only Python's built-in file handling and string processing features without relying on external libraries or the built-in `csv` module.

## How It Works

The solution is divided into two functions.

The `parse_csv()` function reads the input file line by line and yields each row as a list of values.

The `calculate_sums()` function:

- Reads each row from the input CSV file.
- Converts the values to integers.
- Calculates the sum of the row.
- Appends the calculated sum to the end of the row.
- Writes the updated row to a new file named `result.csv`.

## Example

Given the following **input.csv** file:

```text
3, 3, 1, 1, 1, 1, 1
1, 1, 4, 5, 6, 7, 8
1, 5, 6, 7, 4, 3, 1
```

The generated **result.csv** file will contain:

```text
3, 3, 1, 1, 1, 1, 1, 11
1, 1, 4, 5, 6, 7, 8, 32
1, 5, 6, 7, 4, 3, 1, 27
```

## Code

```python
def parse_csv(path: str):
    with open(path) as csv:
        for row in csv:
            yield row.strip().split(',')

def calculate_sums(path: str) -> None:
    with open("result.csv", "w") as out_file:
        for row in parse_csv(path):
            row_list = list(map(int, row))
            row_list.append(sum(row_list))
            new_row = ", ".join(map(str, row_list))
            out_file.write(new_row + "\n")
```

---

**Author:** AiPixelCode
