# method: 1
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break


# method: 2
#The set() method in Python is used to create a set, which is an unordered collection of unique and immutable elements. It is a built-in Python data type that allows you to store multiple items in a single variable, ensuring no duplicates are present.
def find_first_repetitive_char(string):
    seen = set()  # To store characters that have been encountered
    for char in string:
        if char in seen:  # Check if the character is already in the set
            return char  # Return the first repetitive character
        seen.add(char)  # Add the character to the set
    return None  # If no repetitive character is found

# Example usage
string = "programming"
result = find_first_repetitive_char(string)
if result:
    print(f"The first repetitive character is: {result}")
else:
    print("No repetitive characters found.")
