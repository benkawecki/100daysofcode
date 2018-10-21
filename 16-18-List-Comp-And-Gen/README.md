# 16-18 List Comprehension and Generators

## List comprehension
List comprehensions are a pythonic way of generating a list in a short amount of code. See below, previously to generate a list of names that were in the first half of the alphabet a for loop and if statement were use. This generates a large block of code.
```python
# ['pybites', 'mike', 'bob', 'julian', 'tim', 'sara', 'guido']
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
```
This same <code>new_names</code> list can be generated using a list comprehension in one line of code.
```python
[name.title() for name in names if name[0] in first_half_alphabet]
```
Both list are the same, except the second list, generated using list comprehension is much more readable and done in one line of code.

## Generators
A generator function returns an generator object which functions as an iterator.
```python
def num_gen():
    for i in range(5):
        yield i
```
Generator functions must use the yield keyword instead of return. Each time the generator function hits the yield keyword it will break, return the value and remember its place. So next time the function is called with <code>next()</code> it will move on to the next value. If the <code>next()</code> command is called on a generator that has already yielded all its values it will return a <code>StopIteration</code> error. In order to use the generator again a new generator object must be created from the generator function.

Generator function are faster than lists for large datasets because the don't hold all of the values in memory. This is a significant advantage in Large Data.
