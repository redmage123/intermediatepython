class Person:
    def __init__(self, first_name, last_name, age, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    @classmethod
    def from_dict(cls, data):
        first_name = data.get('first_name', 'Unknown')
        last_name = data.get('last_name', 'Unknown')
        age = data.get('age', 0)
        email = data.get('email')
        return cls(first_name, last_name, age, email)

    def __repr__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, age={self.age}, email={self.email})"

# Standard instantiation
person1 = Person("John", "Doe", 30, "john.doe@example.com")
print(person1)

# Instantiation using a dictionary and the class method
data = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25
}
person2 = Person.from_dict(data)
print(person2)

# Instantiation using a dictionary with optional parameters
data_with_optional = {
    'first_name': 'Emily',
    'age': 22,
    'email': 'emily@example.com'
}
person3 = Person.from_dict(data_with_optional)
print(person3)
