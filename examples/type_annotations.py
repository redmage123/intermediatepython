from typing import List, Dict, Tuple, Set, Optional, Union

# Annotating basic types
name: str = "Alice"
age: int = 30
height: float = 5.6
is_married: bool = False

# Annotating list type
def sum_of_elements(numbers: List[int]) -> int:
    return sum(numbers)

# Annotating dictionary type
def get_grade(student_grades: Dict[str, float], student_name: str) -> Optional[float]:
    return student_grades.get(student_name)

# Annotating tuple type
def min_and_max(points: Tuple[int, ...]) -> Tuple[int, int]:
    return min(points), max(points)

# Annotating set type
def unique_elements(items: Set[int]) -> Set[int]:
    return set(items)

# Annotating optional type
def find_divisor(number: int, divisor: Optional[int] = None) -> float:
    if divisor:
        return number / divisor
    return number

# Annotating union type
def add_numbers(a: Union[int, float], b: Union[int, float]) -> float:
    return a + b

# Test the functions
print(sum_of_elements([1, 2, 3, 4]))  # Output: 10
print(get_grade({"Alice": 90, "Bob": 85}, "Alice"))  # Output: 90
print(min_and_max((1, 2, 3, 4, 5)))  # Output: (1, 5)
print(unique_elements({1, 2, 2, 3, 3, 3}))  # Output: {1, 2, 3}
print(find_divisor(10, 2))  # Output: 5.0
print(find_divisor(10))  # Output: 10
print(add_numbers(1, 2.5))  # Output: 3.5
