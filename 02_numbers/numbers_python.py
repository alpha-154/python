# ==============================
# Python Numbers: Beginner to Advanced
# ==============================

# ** Basic Number Types **
# Integers (int), Floating Point Numbers (float), Complex Numbers (complex)

# Integer example
int_num = 42
print("Integer:", int_num)

# Float example
float_num = 3.14
print("Float:", float_num)

# Complex number example
complex_num = 2 + 3j
print("Complex:", complex_num)

# Type Checking
print("Type of int_num:", type(int_num))
print("Type of float_num:", type(float_num))
print("Type of complex_num:", type(complex_num))

# ==============================
# ** Basic Arithmetic Operations **
# ==============================
a, b = 15, 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)  # Always returns a float
print("Floor Division:", a // b)  # Integer division
print("Modulus:", a % b)  # Remainder
print("Exponentiation:", a ** b)  # Power

# ==============================
# ** Built-in Functions for Numbers **
# ==============================

# Absolute Value
print("Absolute Value of -10:", abs(-10))

# Power
print("Power (2^3):", pow(2, 3))

# Rounding
print("Rounding 3.456 to 2 decimal places:", round(3.456, 2))

# Minimum and Maximum
numbers = [4, 7, 1, 9, 12]
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))

# ==============================
# ** Advanced Math Operations (math module) **
# ==============================
import math

# Square root
print("Square root of 16:", math.sqrt(16))

# Logarithms
print("Log base 10 of 100:", math.log10(100))
print("Natural Log of e:", math.log(math.e))

# Trigonometry
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Cosine of 0 degrees:", math.cos(math.radians(0)))

# Constants
print("Value of Pi:", math.pi)
print("Value of Euler's number (e):", math.e)

# ==============================
# ** High Precision Arithmetic (decimal module) **
# ==============================
from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 6  # Precision up to 6 decimal places
decimal_num1 = Decimal('1.123456789')
decimal_num2 = Decimal('2.987654321')
print("Decimal Addition:", decimal_num1 + decimal_num2)

# Decimal Arithmetic
print("Decimal Division:", Decimal('10.5') / Decimal('3.2'))

# ==============================
# ** Working with Arrays of Numbers (numpy module) **
# ==============================
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", arr)

# Array operations
print("Array Addition:", arr + 2)
print("Array Multiplication:", arr * 3)

# Statistical operations
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Sum of all elements:", np.sum(arr))

# Linear Algebra (dot product)
arr2 = np.array([5, 4, 3, 2, 1])
print("Dot Product:", np.dot(arr, arr2))

# ==============================
# ** Random Numbers (numpy.random module) **
# ==============================
# Generate random numbers
random_num = np.random.rand()  # Random float between 0 and 1
print("Random Number (0-1):", random_num)

# Random integers
random_int = np.random.randint(1, 100)  # Random int between 1 and 99
print("Random Integer (1-100):", random_int)

# Random choice from a list
random_choice = np.random.choice(numbers)
print("Random Choice from List:", random_choice)

# ==============================
# ** Complex Numbers Operations **
# ==============================
# Accessing real and imaginary parts
print("Real Part of Complex Number:", complex_num.real)
print("Imaginary Part of Complex Number:", complex_num.imag)

# Complex Conjugate
print("Conjugate of Complex Number:", complex_num.conjugate())

# Magnitude (absolute value) of complex numbers
print("Magnitude of Complex Number:", abs(complex_num))

# ==============================
# ** Tips for Handling Numbers **
# ==============================
# 1. Prefer the `decimal` module for high-precision arithmetic (e.g., financial calculations).
# 2. Use the `numpy` module for operations on large datasets and matrices.
# 3. Use the `math` module for complex mathematical functions.
