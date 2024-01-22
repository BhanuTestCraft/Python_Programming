# Here we are learning about the print statements used in the python
# generally print statements end with the new line or enter due to which all the statements get printed in the new line over the terminal.
print("Hello World")
print("This is Code and Debug")
print("Automation")


# Now if we want to print all the statements in one line then we will use the keyword end inside the print statement.
print("My name is Bhanu Pratap",end=" ")
print("My age is 27",end=" ")
print("My gender is male. ")

name="bhanu"
age=27
# Print using the string literal
# String Literals:

# "Name:", "Age:": These are called string literals. They are fixed pieces of text that will be displayed as-is.
# Variables:

# name, age: These are variables that hold values. In this case, name holds the value "bhanu," and age holds the value 27.
# Commas Between Items:

# The commas , between the items tell Python to separate them when displaying. It means, "Hey, print this, then a space, then the value of name, then another space, then 'Age:', then a space, and finally, the value of age."
print("Name:",name, "Age:",age)

# Print using F-string
# Formatted string literals, commonly known as f-strings, were introduced in Python 3.6 to simplify and enhance string formatting. F-strings provide a concise and readable way to embed expressions within string literals. They are a convenient and efficient way to create formatted strings without the need for complicated syntax or concatenation.

# The f-string is created by prefixing the string with the letter f. Within the f-string, expressions enclosed in curly braces {} are evaluated, and their values are inserted into the string. Here, {name} and {age} are replaced with the values of the respective variables.

# Advantages of f-strings:

# Readability: F-strings make the code more readable by allowing variables and expressions to be directly embedded within the string.
# Conciseness: F-strings are concise and often require less code compared to other string formatting methods.
# Efficiency: F-strings are generally more efficient than other formatting methods in terms of both execution speed and developer time.
formatted_string= f"Name:{name},Age:{age}"
print(formatted_string)
print(f"Name:{name}, Age:{age}")