def multiply(a, b):
    return a * b

def curried_multiply(a):
    def inner(b):
        return multiply(a, b)
    return inner

# Usage
multiply_by_2 = curried_multiply(2)
result = multiply_by_2(3)  # Output should be 6
print(f"Manual Currying Result: {result}")
