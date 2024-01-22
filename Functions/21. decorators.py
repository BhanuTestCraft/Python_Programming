"""
Certainly! Decorators in Python allow you to extend or modify the behavior of functions or methods without changing their source code. They are a powerful and flexible feature that is often used for tasks such as logging, timing, access control, and more. Let's go through a simple example of creating and using a decorator, explaining each line:
"""


# Step 1: Define a decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")

    return wrapper


# Step 2: Use the decorator by applying the @ syntax
@my_decorator
def say_hello():
    print("Hello!")


# Step 3: Call the decorated function
say_hello()

"""
Explanation:

Define a decorator function:

my_decorator is a function that takes another function (func) as an argument.
Inside my_decorator, a new function wrapper is defined. This function will be used to wrap the original function and add additional behavior before and after its execution.
The wrapper function prints messages before and after calling the original function.

Use the decorator by applying the @ syntax:

@my_decorator is a syntactic sugar for say_hello = my_decorator(say_hello). It applies the my_decorator to the say_hello function.
It means that say_hello now points to the wrapper function returned by my_decorator, which includes the original behavior of say_hello plus the additional behavior defined in wrapper.

Call the decorated function:

When you call say_hello(), it is actually calling the wrapper function (due to the decoration).
The wrapper function prints messages before and after calling the original say_hello function.
"""

# output:
"""
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""
