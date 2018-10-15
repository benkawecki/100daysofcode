# 07-09 Data Structures
Python has 3 main data structures built in Lists, Tuples and Dictionaries (sets as a subset of dicts are a 4th type). These data structures can all hold non-homogeneous data types (booleans, strings, int, floats and other data structures).

## lists
Lists are created through enclosing data within square brackets or utilizing the list() function with no arguments or an iterable containing data values.

```python
l1 = [True, 2, "Three", [4]]
l2 = list()
```
The contents of lists can be access by passing an index using square brackets. All data structures within python are 0-indexed. Multiple contents can be accessed at the same time by passing a range separating the first index in the slice and last index in the slice with a colon.
## Tuples
Tuples are created through enclosing data within round brackets or utilizing the tuple() function with no arguments or a iterable containing data values.

```python
t1 = (True, 2, "Three", [4])
t2 = tuple()
```
The contents of tuples can be accessed the same as with lists. The major difference between tuples and Lists is that Tuples are immutable so their contents cannot be changed after be instantilized.

## Dictionaries
Dictionaries are hashtables of key-value pairs. the keys of dictionaries can be any datatype except for a list. Dictionaries can be created either through enclosing key-value pairs with curly brackets or calling dict().

```python
d1 = {'key1':1,'key2':2}
d2 = dict{}
```
Key-value pairs can be added and removed from a dictionary using dictioaries built in methods. Since the keys in a dictionary are hashed they support quick and constant time look ups. 
