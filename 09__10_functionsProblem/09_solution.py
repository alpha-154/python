# Understanding the `yield` Keyword in Python

# The `yield` keyword in Python is used in a generator function to produce a 
# sequence of values lazily, one at a time. A generator function pauses at each 
# `yield` statement and resumes where it left off when called again.

# Code Example:
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

# Key Points About `yield`:

# 1. Generator Function:
#    - A function containing the `yield` keyword is a generator function.
#    - It returns a generator object when called, instead of executing immediately.
#      Example: `even_generator(10)` returns a generator object, not the first value.

# 2. How `yield` Works:
#    - The `yield` statement produces a value and pauses the function execution.
#    - The state of the function (including variables like `i`) is saved.
#    - When the generator's `__next__()` method is called, execution resumes right 
#      after the last `yield`.

# 3. `for` Loop and Generators:
#    - The `for` loop automatically calls the generator's `__next__()` method to 
#      fetch the next value.
#    - Each yielded value is assigned to the loop variable (`num` in this case).
#    - When the generator has no more values to yield, it raises a `StopIteration` 
#      exception, which signals the `for` loop to stop.

# 4. Example Execution:
#    - When `even_generator(10)` is called:
#      - The generator starts iterating over `range(2, 11, 2)` (`2, 4, 6, 8, 10`).
#      - On each iteration:
#        - The current value of `i` is yielded to the loop.
#        - The generator pauses until the next iteration of the `for` loop.
#    - Output:
#      2
#      4
#      6
#      8
#      10

# 5. Lazy Evaluation:
#    - Generators only compute and yield values as needed, which is memory-efficient 
#      for large datasets.

# 6. Difference Between `yield` and `return`:
#    - `return`: Ends the function and returns a value immediately.
#    - `yield`: Pauses the function, saving its state, and returns a value. The 
#      function can resume from where it left off.

# Benefits of Using `yield`:
# - Memory Efficiency: Generates values one at a time instead of creating large 
#   lists in memory.
# - Infinite Sequences: Can represent infinite sequences like an infinite list of 
#   even numbers, as the generator only calculates values when needed.



