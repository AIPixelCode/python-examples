# Word Cleaner and Counter

## Description

This program processes a text, removes invalid characters from words, standardizes their capitalization, and counts the occurrences of the resulting valid words.

A word is considered valid only if more than half of its characters are English letters. Words that do not satisfy this condition are ignored.

## How It Works

The function first splits the input text into individual words using whitespace as the separator.

For each word, it removes all non-alphabetic characters while preserving only English letters.

If the remaining letters make up more than half of the original word, the cleaned word is considered valid. It is then converted to title case so that the first letter is uppercase and the remaining letters are lowercase.

Finally, the function counts how many times each processed word appears and returns the results as a dictionary.

## Example

Given the following input:

```text
hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a
```

The function returns:

```text
{
    'A': 2,
    'For': 1,
    'Friends': 1,
    'Hello': 1,
    'Is': 1,
    'My': 1,
    'Test': 1,
    'This': 1,
    'Your': 1
}
```

## Code

```python
def check_words(text: str) -> dict[str, int]:
    text_list = text.split()
    good_words = {}
    for word in text_list:
        good_word = ''.join(filter(lambda letter: letter.isalpha(), word))
        if len(good_word) > len(word) / 2:
            good_word_title = good_word.title()
            good_words[good_word_title] = good_words.get(good_word_title, 0) + 1
    return good_words
```

---

**Author:** AiPixelCode
