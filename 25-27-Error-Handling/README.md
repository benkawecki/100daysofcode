# 25-27 Error Handling

## Assert
The assert statement lets you check a value. If the value after the assert statement is truthy then the assert statement will pass and the program will continue to the next line. If the value is Falsey then the assert statement will throw an Assertion Error. This allows a program to fail quickly potentially bypassing some other operations.
```python
x = 1
assert x == 1
# passes!
assert x == 2, MyCustomError('Custom error message')
# fails! returns an AssertionError on the stack
```

## Raise
Raise is used to raise an error. typically used in conjunction with the try-except clause listed later. Raise can raise any error derived from python's base error class. You can also include a custom error message for debugging.

```python
if condition:
    # my code here
else:
    raise Error('Custom Error Message!')
```
## Try-Except

```python
try:
    # code that might error
except ValueError:
    # code that runs after value error
except Error:
    # code that runs after any Error
finally:
    # code that always runs even after an except block is run
```
## Exception
Python has a host of base exception that are all derived from the base exception class. These built-in exceptions include ValueErrors and other common error codes (as well as error codes that python needs to function). A list of all python base exceptions can be found [here](https://docs.python.org/3/library/exceptions.html).

Custom exceptions can be derived form the base exception using inheritance.
