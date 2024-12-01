# Python Strings - From Beginner to Advanced

# 1. What is a String?
# A string in Python is a sequence of characters enclosed within single, double, or triple quotes.
# Examples:
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello, 
World!'''  # Can span multiple lines
print(single_quote_string, double_quote_string, triple_quote_string, sep="\n")

# 2. Basic String Operations
string = "Python Programming"

# Length of a string
print(len(string))  # 18

# Accessing characters and slicing
print(string[0])  # 'P' (1st character)
print(string[-1])  # 'g' (last character)
print(string[0:6])  # 'Python'
print(string[7:])  # 'Programming'

# Concatenation and repetition
greeting = "Hello"
name = "Alice"
print(greeting + ", " + name + "!")  # 'Hello, Alice!'
print(greeting * 3)  # 'HelloHelloHello'

# 3. String Methods (Most Common)

# Changing case
print(string.lower())  # 'python programming'
print(string.upper())  # 'PYTHON PROGRAMMING'
print(string.capitalize())  # 'Python programming'
print(string.title())  # 'Python Programming'
print(string.swapcase())  # 'pYTHON pROGRAMMING'

# Searching and replacing
print(string.find("Pro"))  # 7 (index of substring)
print(string.replace("Python", "Java"))  # 'Java Programming'

# Checking string properties
print(string.isalpha())  # False (contains spaces)
print("123".isdigit())  # True
print("abc".islower())  # True
print("Hello".istitle())  # True

# Splitting and joining strings
words = string.split()  # Split by spaces -> ['Python', 'Programming']
print(words)
joined_string = " ".join(words)  # 'Python Programming'
print(joined_string)

# Stripping whitespace
spacey_string = "   Python   "
print(spacey_string.strip())  # 'Python'
print(spacey_string.lstrip())  # 'Python   '
print(spacey_string.rstrip())  # '   Python'

# 4. Advanced String Formatting

# f-strings (from Python 3.6)
age = 25
print(f"My name is {name}, and I am {age} years old.")

# str.format() method
print("My name is {}, and I am {} years old.".format(name, age))

# Padding and alignment
print("{:<10}".format("Left"))  # Left-align
print("{:>10}".format("Right"))  # Right-align
print("{:^10}".format("Center"))  # Center-align

# Precision and number formatting
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")  # '3.14'
print("{:.3f}".format(pi))  # '3.142'

# 5. Useful Escape Characters
print("Hello\nWorld!")  # Newline
print("Hello\tWorld!")  # Tab
print("Backslash: \\")  # Backslash

# 6. Raw Strings
raw_string = r"This is a raw string, no escapes: \n\t"
print(raw_string)

# 7. Strings are Immutable
# Strings cannot be changed in place. Modifications create a new string.
immutable_example = "Immutable"
# immutable_example[0] = 'i'  # This will raise an error
new_string = 'i' + immutable_example[1:]
print(new_string)  # 'immutable'

# 8. Advanced: Working with Strings and Lists
sentence = "Python is fun and versatile."
words_list = sentence.split()  # Converts sentence to list of words
print(words_list)  # ['Python', 'is', 'fun', 'and', 'versatile.']

sorted_words = sorted(words_list)  # Alphabetical order
print(sorted_words)

reversed_sentence = " ".join(reversed(words_list))  # Reverse the word order
print(reversed_sentence)

# 9. Regular Expressions with Strings
import re
text = "Python is awesome. Learn Python!"
pattern = r"Python"
matches = re.findall(pattern, text)
print(matches)  # ['Python', 'Python']
replaced_text = re.sub(pattern, "Java", text)
print(replaced_text)  # 'Java is awesome. Learn Java!'

# 10. Multiline Strings and Docstrings
multi_line = """This is a 
multiline string."""
print(multi_line)

def example_function():
    """
    This is a docstring.
    It describes what the function does.
    """
    pass

print(example_function.__doc__)
