import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

# Using the custom decorator
@timer_decorator
def slow_function(duration):
    print("Starting slow function...")
    time.sleep(duration)
    print("Slow function done.")
    return "Result"

# Call the decorated function
result = slow_function(2)
