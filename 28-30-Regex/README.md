# 28-30 Regular Expressions
The regular expression module is a powerful tool for finding patterns within strings. The module is can be imported using:
```python
import re
```
In order to use REGEX you need to follow the following main workflow:
```python
MyRegex  = re.compile(regex_pattern) #returns a regex object
mo = MyRegex.search(my_string_to_search) #uses the regex object to search the input string.
if mo not None: # the search method will return None if so patterns are found
    print(mo.group()) #will print all of the strings that match the pattern.
```
There are three main methods that are used in conjuction with the regex object. The first, used above, is the search method, second is the match method and last is the findall method.
## Search
The regex search method will look through the given string and then return the first match of the regex.
## Match
The regex match method will start on the first character of the string and attempt to match the regex.
## Findall
The regex findall method will go through the whole string and return a data struct
