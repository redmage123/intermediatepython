class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Create an instance of the Person class
person = Person("Alice", 30)

# Using repr() function to get the developer-friendly string representation
# This will call the __repr__ method
print("Using repr():")
print(repr(person))

# Using str() function to get the user-friendly string representation
# This will call the __str__ method
print("\nUsing str():")
print(str(person))

# Using print() function directly on the object
# This will call the __str__ method by default
print("\nUsing print():")
print(person)

# In a list, the __repr__ method is used for string representation
print("\nIn a list:")
print([person])

# In the interactive interpreter, the __repr__ method is used by default
# Uncomment the following line if you're running this in an interactive session
# person
