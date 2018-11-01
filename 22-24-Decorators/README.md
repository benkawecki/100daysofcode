# 22-24 Decorators

## Decorators
Decorators are an advanced and power topic allowing for the dynamic alternation of a function. This topic is one of the 23 GoF design patterns. A basic decorator function is shown below.

```python
def decorator_function(f):
    def wrapper_function(*args, **kwargs):
        # something to execute before the decorated function
        result = f(*args, **kwargs)
        # something to execute after the decorated function
        return result
    return wrapper_function
```
The decorator function takes a function object as an argument. It then returns the wrapper function within. When a function is decorated, it will be calling the wrapper function instead of the original function.
```python
@decorator_function
def my_func():
    pass
# same as decorator_function(my_func)
```
Decorators allow for an additional layer of abstraction which can be applied over a variety of different functions at runtime.

## Decorators with Arguments
Decorators with arguments must apply an additional wrapper layer.
```python
def decorator_function_with_arguments(arg1, arg2):
    def wrap(f):
        def wrapper(*args, **kwargs):
            # something to execute before the decorated function with arg1/arg2
            result = f(*args, **kwargs)
            # something to execute after the decorated function with arg1/arg2
            return result
        return wrapper
    return wrap
```
I am not sure how this additional layer adds the functionality of arguments
