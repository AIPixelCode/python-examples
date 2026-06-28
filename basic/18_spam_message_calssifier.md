# Spam Message Classifier

## Description

This program classifies messages into different categories based on the validity of the sender's identifier and the message content.

A message is evaluated using two independent validation rules. Based on the results, it is classified as one of the following:

* **Not Spam**
* **Invalid Sender**
* **Invalid Content**
* **Fully Invalid**

## How It Works

The program first validates the sender's identifier.

A sender is considered invalid if the identifier consists entirely of digits. Otherwise, it is treated as valid.

Next, the program evaluates the message content. A message is considered invalid only if **both** of the following conditions are satisfied:

* More than half of its characters are neither letters, digits, nor spaces.
* It contains the word `"spam"` (case-insensitive).

Finally, the sender validation and content validation results are combined to determine the appropriate classification.

## Example

### Example 1

```text
Sender:
@first-user1999

Message:
$#a@5 Spam)--(*^
```

Output:

```text
Invalid Content
```

### Example 2

```text
Sender:
190482184

Message:
Hello (spam) Python
```

Output:

```text
Invalid Sender
```

## Source Code

**File:** `spam_message_classifier.py`

---

**Author:** AiPixelCode
