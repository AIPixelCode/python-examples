# Exception Transformation with Proxy Objects

## Description

This program demonstrates exception handling in Python by transforming the result of function calls into proxy objects.

Instead of allowing exceptions to interrupt the program, each function call produces an `ExceptionProxy` object that stores either a success message or the exception message along with a reference to the corresponding function.

## How It Works

The program defines an `ExceptionProxy` class to represent the outcome of a function call.

A list of functions is passed to the `transform_exceptions()` function. Each function is executed inside a `try-except` block.

If a function executes successfully, an `ExceptionProxy` object is created with the message `"ok!"`. If an exception occurs, another `ExceptionProxy` object is created containing the exception message.

Finally, the function returns a list of `ExceptionProxy` objects, preserving the order of the original function list.

## Example

The following example executes two functions, where one raises an exception and the other completes successfully.

The program produces:

```text
function name: f
message: division by zero
----------
function name: g
message: ok!
----------
```

## Source Code

**File:** `3_exception_transformation_with_proxy_objects.py`

---

#### Author: AiPixelCode
