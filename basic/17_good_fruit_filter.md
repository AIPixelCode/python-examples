# Good Fruit Filter

## Description

This program filters a collection of fruits based on predefined physical characteristics and counts the occurrences of each valid fruit.

Each fruit is represented as a dictionary containing its name, shape, mass, and volume. Only fruits that satisfy all required conditions are included in the final result.

## How It Works

The function iterates through each fruit in the input collection and evaluates the following conditions:

* The fruit must have a spherical shape.
* Its mass must be between **300** and **600** grams (inclusive).
* Its volume must be between **100** and **500** cubic centimeters (inclusive).

Whenever a fruit satisfies all conditions, its name is added to the result dictionary. If the same fruit appears multiple times, its occurrence count is incremented.

After processing all fruits, the function returns a dictionary containing the names of all valid fruits and the number of times each one appears.

## Example

Given the following input:

```text
(
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}
)
```

The valid fruits are:

```text
apple
lemon
apple
```

Therefore, the function returns:

```text
{'apple': 2, 'lemon': 1}
```

## Code

```python
def good_fruits(fruits: tuple[dict]) -> dict[str, int]:
    good = {}
    for fruit in fruits:
        if (
            fruit['shape'] == 'sphere'
            and 300 <= fruit['mass'] <= 600
            and 100 <= fruit['volume'] <= 500
        ):
            good[fruit['name']] = good.get(fruit['name'], 0) + 1
    return good
```

---

**Author:** AiPixelCode
