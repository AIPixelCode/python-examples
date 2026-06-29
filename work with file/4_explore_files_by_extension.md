# Explore Files by Extension

## Description

This program recursively explores a directory and counts the number of files with a specified extension.

The search includes all subdirectories, and the result is returned as a dictionary where each key represents a directory containing matching files and each value represents the number of matching files found directly inside that directory.

File extension matching is performed in a case-insensitive manner.

## How It Works

The program traverses the directory tree using `os.walk()`.

For each directory:

* All files are examined.
* File names are compared with the requested extension without considering letter case.
* Matching files are counted.
* Directories containing at least one matching file are added to the result dictionary.

Finally, the function returns a dictionary containing the matching directories and their corresponding file counts.

## Example

Suppose the directory structure is:

```text
test_media/
├── IMG_2235.jpg
├── travel_photos/
│   ├── IMG_20171017_052418.jpg
│   ├── 20180311_214539.JPG
│   ├── IMG_2237.jpg
│   └── note.txt
└── vid1/
    ├── images/
    └── VID_20170425_184731.mp4
```

Calling:

```python
explore("jpg", "test_media")
```

Returns:

```python
{
    "test_media": 1,
    "test_media/travel_photos": 3
}
```

## Code

```python
import os

def explore(extension: str, directory_path: str) -> dict[str, int]:
    result = {}
    extension = extension.lower()
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(f".{extension}"):
                result[root] = result.get(root, 0) + 1
    return result
```

---

**Author:** AiPixelCode
