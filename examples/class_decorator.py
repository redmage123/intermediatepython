import functools

def log_method_calls(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)

        def __getattribute__(self, name):
            attr = super().__getattribute__("_instance").__getattribute__(name)
            if callable(attr):
                @functools.wraps(attr)
                def wrapper(*args, **kwargs):
                    print(f"Calling method {name} with arguments {args} and keyword arguments {kwargs}")
                    result = attr(*args, **kwargs)
                    print(f"Method {name} returned {result}")
                    return result
                return wrapper
            return attr
    return Wrapped

# Using the custom class decorator
@log_method_calls
class MyClass:
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print(f"The value is {self.value}")

    def add(self, x):
        return self.value + x

# Create an instance of the decorated class
my_instance = MyClass(42)

# Call methods of the class
my_instance.show_value()
result = my_instance.add(8)
