# 04-06 Collections

import from the collections module

``` python
from collections import defaultdict, namedtuple, counter, deque
```

## Named tuple
Convenient way to create Class without methods. Named touples are the same as normal touples except their values can be access with .fieldname. Named touples are still immutable and can still be iterated over. They present an alternative to creating read only classes.

```python
#create a named touple
User = namedtuple(user, role)
user = User(myuser,myrole)
```

here there is much more contextual information about the NamedTouples values, specific variables can now be called by .fieldname instead of their position.

## default dict
A defualtdict is a handy way to get around key errors. When a defaultdict is created it must be initialized with a function('default factory') which takes no arguments. When a key without a value is passed to the dictionary it will not raise a keyerror, instead it will return the function called. It will then save the key value pair in the dictionary

```python
challenges = defaultdict(f)
#note that defaultdict is only pass the function object and not a called function
```
Defaultdict's are very usefult when dealing with lists as values because you can apply list methods to values without conditional code to check if a key is in the dictionary.

## counter
The counter is a subclass of dictionary that takes in any hashable objects. These objects are then stored in a specicial dictionary subclass that supports convenient and rapid counting.

```python
Counter(mylist) #where mylist is some collection of hashable objects
```

Counter will not raise keyerrors when a valueless key is referenced instead it will return 0.

Counter supports unique methods for easy counting these include .most_common([n]) which returns the n most common keys the their counts from the original object. Counter also has an Elements method which returns a list of all of the keys equal to their frequency (i.e. if their were 4 counts of the letter 'a' then the list would contain ['a','a','a'.'a'...])

## deque
Deques (pronounced 'decks' and is short for double-ended queues) are a list like object that is optimized for appends and pops at both "ends" of the object. Deques are more efficient than lists during length-changing operations



## follow-up
chainmaps
ordereddictionary
