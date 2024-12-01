# Python Classes: Beginner to Advanced
# =====================================

# Classes are a way to create your own objects in Python. They are like blueprints for objects.
# Let's explore classes step-by-step, from basic to advanced concepts.

# 1. Defining a Simple Class
class MyClass:
    """A simple example class."""
    def __init__(self, name):  # Constructor method
        self.name = name      # Instance variable

    def greet(self):          # Instance method
        return f"Hello, {self.name}!"

# Usage
obj = MyClass("Alice")
print(obj.greet())  # Output: Hello, Alice!

# --------------------------------------------

# 2. Class vs Instance Variables
class Example:
    class_variable = "I am a class variable"  # Shared by all instances

    def __init__(self, value):
        self.instance_variable = value  # Specific to each instance

# Usage
example1 = Example(42)
example2 = Example(99)
print(example1.class_variable)        # Output: I am a class variable
print(example1.instance_variable)     # Output: 42
print(example2.instance_variable)     # Output: 99

# Modifying the class variable affects all instances
Example.class_variable = "New Value"
print(example1.class_variable)        # Output: New Value

# --------------------------------------------

# 3. Private Variables and Name Mangling
class PrivateExample:
    def __init__(self):
        self.__private_variable = "This is private"

    def get_private(self):
        return self.__private_variable

# Usage
private_obj = PrivateExample()
print(private_obj.get_private())       # Output: This is private
# print(private_obj.__private_variable)  # AttributeError
print(private_obj._PrivateExample__private_variable)  # Output: This is private (using name mangling)

# --------------------------------------------

# 4. Class Methods and Static Methods
class MethodExample:
    class_variable = "Class Variable"

    @classmethod
    def class_method(cls):
        return f"Accessing: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "This is a static method"

# Usage
print(MethodExample.class_method())   # Output: Accessing: Class Variable
print(MethodExample.static_method())  # Output: This is a static method

# --------------------------------------------

# 5. Inheritance
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

# Usage
child = Child()
print(child.greet())  # Output: Hello from Child

# --------------------------------------------

# 6. Polymorphism
class Animal:

    # here pass statement in Python is a placeholder that does nothing. 
    # It’s used when a statement is syntactically required but you don’t 
    # want to execute any code.


    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# Output:
# Woof
# Meow

# --------------------------------------------

# 7. Abstract Classes
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class ConcreteDog(AbstractAnimal):
    def speak(self):
        return "Woof from Abstract Dog"

# Usage
abstract_animal = ConcreteDog()
print(abstract_animal.speak())  # Output: Woof from Abstract Dog

# --------------------------------------------

# 8. Properties (Getters and Setters)
class PropertyExample:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value

# Usage
prop_example = PropertyExample(10)
print(prop_example.value)  # Output: 10
prop_example.value = 20
print(prop_example.value)  # Output: 20
# prop_example.value = -10  # Raises ValueError

# --------------------------------------------

# 9. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)  # Output: Vector(4, 6)

# --------------------------------------------

# 10. Customizing Class Behavior (Magic Methods)
class CustomClass:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"CustomClass with data: {self.data}"

    def __len__(self):
        return len(self.data)

# Usage
custom = CustomClass([1, 2, 3])
print(str(custom))  # Output: CustomClass with data: [1, 2, 3]
print(len(custom))  # Output: 3

# --------------------------------------------

# 11. Metaclasses (Advanced)
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by_metaclass'] = True
        return super().__new__(cls, name, bases, dct)

class MyMetaClass(metaclass=Meta):
    pass

# Usage
meta_instance = MyMetaClass()
print(hasattr(meta_instance, 'created_by_metaclass'))  # Output: True

# =====================================
# This concludes the tutorial on Python classes from beginner to advanced concepts.
