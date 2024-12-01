# Python Tuples - From Basics to Advanced

# 1. What is a Tuple?
# A tuple is an immutable, ordered collection of elements.
# Elements of a tuple can be of any data type, and tuples can be nested.

# Creating a tuple
empty_tuple = ()  # Empty tuple
single_element_tuple = (42,)  # Tuple with one element (note the comma!)
mixed_tuple = (1, "hello", 3.14, True)

print(empty_tuple)           # ()
print(single_element_tuple)  # (42,)
print(mixed_tuple)           # (1, 'hello', 3.14, True)

# Accessing elements
print(mixed_tuple[0])  # 1
print(mixed_tuple[-1])  # True
print(mixed_tuple[1:3])  # ('hello', 3.14)

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0])  # 3

# 2. Immutability of Tuples
# Tuples cannot be changed after creation
example_tuple = (1, 2, 3)
# example_tuple[0] = 10  # This will raise a TypeError

# However, if a tuple contains a mutable element (like a list), the mutable element can be modified.
mutable_inside_tuple = (1, [2, 3], 4)
mutable_inside_tuple[1][0] = 99
print(mutable_inside_tuple)  # (1, [99, 3], 4)

# 3. Tuple Methods
# Tuples have only two methods: count() and index()
numbers = (1, 2, 3, 1, 4, 1)

# Count occurrences of an element
print(numbers.count(1))  # 3

# Find the first index of an element
print(numbers.index(3))  # 2

# 4. Unpacking Tuples
# Assigning tuple elements to variables
person = ("Alice", 25, "Engineer")
name, age, job = person
print(name)  # Alice
print(age)   # 25
print(job)   # Engineer

# Using the * operator to unpack
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# 5. Using Tuples as Keys in Dictionaries
# Tuples can be used as dictionary keys because they are immutable
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
}
print(locations[(40.7128, -74.0060)])  # New York

# 6. Returning Multiple Values from Functions
# Tuples are often used to return multiple values from functions
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([3, 1, 4, 1, 5, 9])
print(result)  # (1, 9)

# Tuple unpacking with function results
min_value, max_value = min_max([3, 1, 4, 1, 5, 9])
print(min_value)  # 1
print(max_value)  # 9

# 7. Tuple Comprehensions (Generator Expression)
# Tuples do not have comprehensions, but you can use generator expressions
numbers = (x ** 2 for x in range(5))
print(tuple(numbers))  # (0, 1, 4, 9, 16)

# 8. Tuples vs Lists
# Tuples are faster than lists due to immutability and simpler structure.
# Use tuples when you need:
# - Fixed, unchangeable data
# - A lightweight alternative to a list
# - To use as dictionary keys

# Example: Using a tuple as a fixed configuration
config = ("localhost", 8080)

# 9. Advanced Use Cases

# a. Named Tuples (from the `collections` module)
# Named tuples provide a way to define simple classes with immutability
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(3, 4)
print(p1)       # Point(x=3, y=4)
print(p1.x)     # 3
print(p1.y)     # 4

# b. Swapping Variables
a, b = 5, 10
a, b = b, a  # Swaps values without a temporary variable
print(a, b)  # 10, 5

# c. Tuples in Sets
# Tuples can be elements of a set, while lists cannot
tuple_set = {(1, 2), (3, 4), (1, 2)}
print(tuple_set)  # {(1, 2), (3, 4)}

# 10. Tuple Performance
# Tuples are more memory-efficient and faster to iterate over compared to lists
import sys
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_example))  # Size of the list in bytes
print(sys.getsizeof(tuple_example))  # Size of the tuple in bytes

# Tuples are immutable, so they have fewer operations than lists, making them faster for certain use cases.

# Summary:
# - Tuples are immutable, ordered collections.
# - Useful for fixed data, dictionary keys, and lightweight structures.
# - Support basic operations: indexing, slicing, unpacking, and iteration.
# - Limited methods (`count`, `index`), but highly efficient and versatile.

# End of File
