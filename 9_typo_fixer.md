# Typo Fixer (Backspace as Equals Sign)

---
## Description:
___While typing a string, the user accidentally pressed the equals sign (=) 
instead of the Backspace key to delete incorrect characters. Write a function 
that takes this mistyped string as input and returns the corrected string.___

> **Rule:** Each = acts as a Backspace, deleting the last valid character 
(if one exists). Multiple consecutive = characters each remove one character.

---
## Python code:

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
## Test:
```python
print(typo_fix('helll=0'))        # hello
print(typo_fix('testtwoo===wo'))  # testtwo
print(typo_fix('===tt=hrehh==e')) # three
```

---
#### Written by: ___AiPixelCode___