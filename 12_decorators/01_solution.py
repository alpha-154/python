# This Python script demonstrates how a decorator works by timing the execution of a function.

import time

# Define the decorator function
def timer(func):
    # This function takes another function 'func' as an argument and returns a new function 'wrapper'
    def wrapper(*args, **kwargs):
        # Record the start time before executing the original function
        start = time.time()
        # Execute the original function with its arguments
        result = func(*args, **kwargs)
        # Record the end time after the function finishes execution
        end = time.time()
        # Calculate and print the runtime of the original function
        print(f"{func.__name__} ran in {end-start} time")
        # Return the result of the original function
        return result
    # Return the wrapper function to replace the original function
    return wrapper

# Use the @timer decorator to wrap the 'example_function'
@timer
def example_function(n):
    # Simulate a task by pausing execution for 'n' seconds
    time.sleep(n)

# Call the decorated function to see the timing functionality in action
example_function(2)

# When you call 'example_function(2)', the decorator 'timer' modifies its behavior.
# Here's what happens:
# 1. 'example_function' is passed as an argument to the 'timer' function.
# 2. The 'timer' function returns the 'wrapper' function, which adds timing logic around the original function.
# 3. When 'example_function(2)' is called, it is actually calling 'wrapper'.
# 4. The 'wrapper' records the time, executes the original function, and calculates the runtime.
# 5. The runtime is printed to the console in this format:
#    example_function ran in 2.0 time
# 6. If the original function had a return value, it would be returned by 'wrapper'.
