def make_counter(start=0, step=1):
    count = start
    def counter():
        nonlocal count
        current = count
        count += step
        return current
    return counter

# Create different counters
counter1 = make_counter(start=0, step=1)
counter2 = make_counter(start=100, step=10)

# Use the counters
print(counter1())  # Output: 0
print(counter1())  # Output: 1
print(counter1())  # Output: 2

print(counter2())  # Output: 100
print(counter2())  # Output: 110
print(counter2())  # Output: 120
