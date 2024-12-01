# method : 1
input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str  

print(reversed_str)

# method : 2
input_str = "Python"
reversed_str = input_str[::-1]

print(reversed_str)