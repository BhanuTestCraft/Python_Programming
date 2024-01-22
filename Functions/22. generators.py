"""
Generators in Python are a way to create iterators using a function with the yield statement. They allow you to iterate over a potentially large sequence of data without creating the entire sequence in memory at once. This can be more memory-efficient compared to using lists.
"""


# Example: Generating Fibonacci Sequence using a Generator
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Using the generator to generate the first 5 Fibonacci numbers
fibonacci_gen = fibonacci_generator(5)

# Iterating over the generator
for number in fibonacci_gen:
    print(number)

"""
Explanation:

Generator Function:
fibonacci_generator is a generator function that uses the yield statement to produce a sequence of Fibonacci numbers.
The function starts with two variables a and b initialized to 0 and 1, representing the first two numbers in the Fibonacci sequence.

yield Statement:
The yield statement is used to produce a value (a) to the caller and pause the function's execution. The state of the function is preserved.

Using the Generator:
fibonacci_gen = fibonacci_generator(5) creates a generator object that will produce the first 5 Fibonacci numbers.

Iterating over the Generator:
The for loop iterates over the generator, and each time it requests the next value, the generator function resumes from where it left off.
"""

# output:
"""
0
1
1
2
3
"""

# Generators are beneficial when dealing with large datasets or infinite sequences, as they allow you to generate values on-the-fly without storing the entire sequence in memory. Additionally, generators are lazy, meaning they only generate values when requested, making them memory-efficient.
