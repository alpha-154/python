# method: 01
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)


# method: 02
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):  # Start from 2 since multiplying by 1 has no effect
        result *= i
    return result

# Example usage
number = 5
print(f"The factorial of {number} is: {factorial(number)}")

# Output: The factorial of 5 is: 120


# method: 03
# finding the factorials of numbers from 1 to 7

print("factorial from 1 to N")
def factorials_up_to_n(n):
    if n < 1 or n >= 20:
        return "n should be a positive integer less than 20"
    
    factorials = [1]  # 0! = 1, so we start the list with 1
    for i in range(2, n + 1):  # Start from 2 to n (1! is already in the list)
        factorials.append(factorials[-1] * i)  # Multiply the last factorial with i to get the next one
    
    return factorials

# Example usage
n = 7
result = factorials_up_to_n(n)
print(f"Factorials from 1 to {n}: {result}")
