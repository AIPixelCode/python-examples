# Typo Fixer

## Description

This program corrects text in which the equals sign (`=`) has been mistakenly used instead of the Backspace key.

Each `=` character is treated as a backspace operation and removes the most recently entered valid character. The function processes the input string and returns the corrected result.

## How It Works

The function scans the input string one character at a time.

* Regular characters are added to a temporary output buffer.
* When an `=` character is encountered, the most recently stored character is removed, if one exists.
* Consecutive `=` characters perform multiple backspace operations.

After processing the entire string, the remaining characters are combined to form the corrected text.

## Example

```text
Input:  helll=o
Output: hello
```

```text
Input:  testtwoo===wo
Output: testtwo
```

```text
Input:  ===tt=hrehh==e
Output: three
```

## Code

```python
def typo_fix(st):
    out = []

    for s in st:
        if s == '=':
            if len(out) != 0:
                out.pop()
        else:
            out.append(s)

    return ''.join(out)
```

---

**Author:** AiPixelCode
