# 10-12 Pytest
pytest is a framework for writing tests for python code


## unittest
unittest is pythons built in testing library

## pytest
pytest will run all files of the form test_*.py or \*\_test.py in the library and all sub-libraries.

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5Â
```
