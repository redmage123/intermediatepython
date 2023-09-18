from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        f(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")

print(say_hello.__name__)  # Output: 'say_hello'
print(say_hello.__doc__)   # Output: 'Say hello to someone.'
