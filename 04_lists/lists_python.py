# Python Lists - From Beginner to Advanced

# 1. What is a List?
# A list is a mutable, ordered collection of items that can hold different data types.
# Examples:
empty_list = []
numbers = [1, 2, 3, 4]
mixed_list = [1, "hello", 3.5, True]

print(numbers)
print(mixed_list)

# 2. Basic Operations with Lists
# Indexing and slicing
print(numbers[0])  # First element -> 1
print(numbers[-1])  # Last element -> 4
print(numbers[1:3])  # Slicing -> [2, 3]

# Adding elements
numbers.append(5)  # Add at the end
print(numbers)  # [1, 2, 3, 4, 5]

numbers.insert(2, 10)  # Insert at index 2
print(numbers)  # [1, 2, 10, 3, 4, 5]

# Removing elements
numbers.remove(10)  # Remove by value
print(numbers)  # [1, 2, 3, 4, 5]

popped = numbers.pop()  # Remove the last element
print(popped, numbers)  # 5 [1, 2, 3, 4]

del numbers[1]  # Delete element at index 1
print(numbers)  # [1, 3, 4]

# Clearing the list
numbers.clear()
print(numbers)  # []

# 3. Iterating Through a List
fruits = ["apple", "banana", "cherry"]

# Using a for loop
for fruit in fruits:
    print(fruit)

# Using enumerate for index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 4. Common List Methods
numbers = [3, 1, 4, 1, 5]

# Adding elements
numbers.append(9)  # Add one element
numbers.extend([2, 6])  # Add multiple elements
print(numbers)  # [3, 1, 4, 1, 5, 9, 2, 6]

# Sorting and reversing
numbers.sort()  # Sort ascending
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)  # Sort descending
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

numbers.reverse()  # Reverse the list
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Counting occurrences
print(numbers.count(1))  # 2 occurrences of 1

# Finding index
print(numbers.index(4))  # Index of first occurrence of 4 -> 4

# Copying a list
new_numbers = numbers.copy()
print(new_numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 5. List Comprehensions
# Creating a new list from an existing one
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Filtering a list
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# 6. Advanced List Operations

# Using `zip` to combine two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined = list(zip(list1, list2))
print(combined)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Flattening a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # [1, 2, 3, 4, 5, 6]

# Using `map` and `filter`
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

filtered_numbers = list(filter(lambda x: x > 2, numbers))
print(filtered_numbers)  # [3, 4, 5]

# 7. Useful Libraries for Lists
import numpy as np

# Converting a list to a numpy array
numpy_array = np.array(numbers)
print(numpy_array)  # [1 2 3 4 5]

# Performing operations with numpy
print(numpy_array + 10)  # [11 12 13 14 15]

# Using itertools for advanced operations
from itertools import permutations, combinations

# Permutations
perm = list(permutations(numbers, 2))
print(perm)  # [(1, 2), (1, 3), ...]

# Combinations
comb = list(combinations(numbers, 2))
print(comb)  # [(1, 2), (1, 3), ...]

# 8. Tips and Tricks
# Checking if a list is empty
if not numbers:
    print("List is empty")

# Cloning a list
cloned_list = numbers[:]  # Alternative to .copy()

# Sorting without modifying the original list
sorted_list = sorted(numbers)
print(sorted_list)
