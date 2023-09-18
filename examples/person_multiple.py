class PersonStandard:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"PersonStandard(name={self.name}, age={self.age})"

# Create an instance and print it
person_standard = PersonStandard("Alice", 30)
print("Standard Class:", person_standard)


from collections import namedtuple

PersonNamedTuple = namedtuple("PersonNamedTuple", ["name", "age"])

# Create an instance and print it
person_namedtuple = PersonNamedTuple("Bob", 40)
print("Named Tuple:", person_namedtuple)


from dataclasses import dataclass

@dataclass
class PersonDataClass:
    name: str
    age: int

# Create an instance and print it
person_dataclass = PersonDataClass("Charlie", 50)
print("Dataclass:", person_dataclass)
