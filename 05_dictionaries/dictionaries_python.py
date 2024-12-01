# Python Dictionaries - From Beginner to Advanced

# 1. What is a Dictionary?
# A dictionary in Python is an unordered collection of key-value pairs.
# Each key is unique, and the values can be of any data type.

# Creating a dictionary
empty_dict = {}  # Empty dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print(person["name"])  # Alice
# Using .get() to avoid KeyError if the key doesn't exist
print(person.get("name"))  # Alice
print(person.get("country", "Not Found"))  # Not Found (default value)

# Adding and updating key-value pairs
person["job"] = "Engineer"  # Add a new key
person["age"] = 26  # Update an existing key
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

# Removing elements
del person["city"]  # Remove using del
print(person)  # {'name': 'Alice', 'age': 26, 'job': 'Engineer'}

person.pop("age")  # Remove and return value for a key
print(person)  # {'name': 'Alice', 'job': 'Engineer'}

# Clearing all elements
person.clear()
print(person)  # {}

# 2. Iterating Through a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Iterating through keys
for key in person:
    print(key, "->", person[key])

# Iterating through values
for value in person.values():
    print(value)

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# 3. Dictionary Methods
numbers = {"one": 1, "two": 2, "three": 3}

# Copying a dictionary
numbers_copy = numbers.copy()
print(numbers_copy)  # {'one': 1, 'two': 2, 'three': 3}

# Updating a dictionary
numbers.update({"four": 4, "five": 5})  # Add multiple key-value pairs
print(numbers)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Removing a random key-value pair
removed_item = numbers.popitem()
print(removed_item)  # ('five', 5) (random key-value pair removed)
print(numbers)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# Checking for keys
print("one" in numbers)  # True
print("six" in numbers)  # False

# 4. Dictionary Comprehensions
# Create a dictionary from a list
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering items
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 5. Nested Dictionaries
# A dictionary can contain another dictionary as a value.
students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 30, "city": "San Francisco"},
}
print(students["Alice"]["age"])  # 25

# Adding a new nested dictionary
students["Charlie"] = {"age": 35, "city": "Chicago"}
print(students)

# Iterating through a nested dictionary
for student, details in students.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key} -> {value}")

# 6. Advanced Operations with Dictionaries

# Using `defaultdict` from the `collections` module
from collections import defaultdict

# defaultdict automatically assigns a default value for missing keys
default_dict = defaultdict(int)
default_dict["a"] += 1
print(default_dict)  # {'a': 1}

# Using `Counter` for counting elements
from collections import Counter

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = Counter(fruits)
print(fruit_count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Using `OrderedDict` to maintain order of keys (Python 3.7+ does this by default)
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["one"] = 1
ordered_dict["two"] = 2
ordered_dict["three"] = 3
print(ordered_dict)  # OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# Using `ChainMap` to combine multiple dictionaries
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
combined = ChainMap(dict1, dict2)
print(combined["b"])  # 2 (value from dict1)
print(combined["c"])  # 4 (value from dict2)

# 7. Merging Dictionaries
# Python 3.9+ supports the `|` operator for merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # Keys in dict2 overwrite keys in dict1
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# 8. Tips and Tricks
# Using `zip` to create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Sorting a dictionary by keys or values
unsorted_dict = {"b": 2, "a": 1, "c": 3}
sorted_by_keys = dict(sorted(unsorted_dict.items()))
print(sorted_by_keys)  # {'a': 1, 'b': 2, 'c': 3}

sorted_by_values = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)  # {'a': 1, 'b': 2, 'c': 3}
