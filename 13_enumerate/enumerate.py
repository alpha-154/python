# This Python script explains the `enumerate` function in Python with examples.

# The `enumerate` function is a built-in utility that allows you to iterate over a sequence 
# (like a list, tuple, or string) while keeping track of both the index and the corresponding value.

# Syntax:
# enumerate(iterable, start=0)
# - `iterable`: Any object that can return its elements one at a time (e.g., a list, tuple, or string).
# - `start` (optional): The starting value of the index (default is 0).

# Example 1: Basic Use
fruits = ["apple", "banana", "cherry"]
# Using enumerate to get both index and value
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# Example 2: Custom Start Index
# You can specify a custom starting index using the 'start' parameter.
for index, fruit in enumerate(fruits, start=1):
    print(f"Position: {index}, Fruit: {fruit}")
# Output:
# Position: 1, Fruit: apple
# Position: 2, Fruit: banana
# Position: 3, Fruit: cherry

# Example 3: Converting to a List
letters = ["a", "b", "c"]
# Converting an enumerate object to a list of tuples
enumerate_object = enumerate(letters)
enumerate_list = list(enumerate_object)
print(enumerate_list)
# Output:
# [(0, 'a'), (1, 'b'), (2, 'c')]

# Example 4: Using with Strings
word = "hello"
# Iterating over a string with enumerate to get both character and index
for index, char in enumerate(word):
    print(f"Character '{char}' is at index {index}")
# Output:
# Character 'h' is at index 0
# Character 'e' is at index 1
# Character 'l' is at index 2
# Character 'l' is at index 3
# Character 'o' is at index 4

# Key Advantages of `enumerate`:
# 1. Eliminates the need for manually managing a counter.
# 2. Results in cleaner and more readable code when both index and value are needed.
# 3. Works with any iterable, making it versatile.
