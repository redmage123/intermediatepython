from functools import partial

def multiply(a, b):
    return a * b

# Usage
multiply_by_2 = partial(multiply, 2)
result = multiply_by_2(3)  # Output should be 6
print(f"Currying using functools.partial Result: {result}")
