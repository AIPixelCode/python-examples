# Simulating Variable Assignment and Print Statements

## Description

This example simulates two basic instructions of a simple programming language.

The program processes a sequence of commands, stores variables in memory, and prints selected values from previously defined variables.

Two types of instructions are supported:

- Variable assignment (`:=`)
- Print statements (`print`)

Variables may contain either a list of integers or a dictionary that maps strings to integers.

## How It Works

The program reads commands one by one and maintains an execution environment using a Python dictionary.

For assignment statements:

- The variable name is extracted.
- The assigned value is converted into a native Python object using `json.loads()`.
- The resulting object is stored in memory.

For print statements:

- The target variable and its index or key are extracted.
- The requested value is retrieved from the stored object.
- The value is printed to the output.

## Example

Given the following input:

```text
4
a := [1, 2, 3]
b := {"2": 1, "1": 4, "4": 5}
print a[1]
print b["1"]
```

The program prints:

```text
2
4
```

## Code

The complete source code is available in **3_simlating_variable_assignment_and_print.py**.

---

**Author:** AiPixelCode
