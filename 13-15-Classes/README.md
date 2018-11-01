# 13-15 Classes
Python is an object orient programing language which features classes/inheritance/polymorphism/metaclasses

## Classes
Classes allow you to efficiently represent a real-world object in a organized fashion. Classes can be created using the class keyword. Classes may have methods associated with them. Python includes a number of methods that are built into the language and allow objects of classes to interact with python's base functions. These methods are called double underscore (dunder) methods and have leading and trailing double underscores (\__method__).
```python
class Creature():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return (f'{self.name} of {self.power} power')

    def train(self):
        self.power += 5
```
Included above are two basic dunder methods. \__init__ is call every time a new object is instantiated from the class. The \__repr__ method is called whenever the object instance is printed to the screen. There are many dunder methods build into the python, additional dunder methods can be created by the user. Traditionally user created dunder methods are for the internal use of the class and not to be called directly. These are comparable to private methods in other language, though, there is no restriction to actually calling these methods, it is just convention.

An object can be created by calling the name of the class which then returns a class instance. \__init__ is called automatically while initializing the class. The python print function will be default look for a \__repr__ or \__str__ method and print the returned result. Then at the end our custom train method is called to increase the power of our creature.

```python
person = Creature('person',10)
print(person)
person.train()
```
## Inheritance

## Polymorphism
