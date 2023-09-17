
import asyncio

async def sum_numbers(numbers):
    """Coroutine that calculates the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
        await asyncio.sleep(0.1)  # simulate some work
    return total

async def main():
    """Main coroutine that schedules the sum_numbers coroutine."""
    numbers = [1, 2, 3, 4, 5]
    sum_coroutine = sum_numbers(numbers)
    result = await sum_coroutine
    print(f'The sum of {numbers} is {result}')

if __name__ == '__main__':
    asyncio.run(main())
