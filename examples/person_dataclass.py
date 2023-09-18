from dataclasses import dataclass, field

@dataclass
class Person:
    # Static variables
    population: int = 0
    all_names: list = field(default_factory=list, init=False, repr=False)

    # Instance variables
    name: str
    age: int
    email: str = 'N/A'
    is_married: bool = False

    def __post_init__(self):
        # Increment the population count and add name to all_names list
        Person.population += 1
        Person.all_names.append(self.name)

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    @classmethod
    def get_population(cls) -> str:
        return f"The current population is {cls.population}."

    @classmethod
    def get_all_names(cls) -> str:
        return f"All names: {', '.join(cls.all_names)}"

# Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 40, "bob@example.com")
person3 = Person("Charlie", 50, "charlie@example.com", True)

# Call instance method
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# Call class methods
print(Person.get_population())  # Output: The current population is 3.
print(Person.get_all_names())  # Output: All names: Alice, Bob, Charlie

# Access static variables directly
print("Directly accessing static variables:")
print("Population:", Person.population)  # Output: Population: 3
print("All Names:", Person.all_names)  # Output: All Names: ['Alice', 'Bob', 'Charlie']
