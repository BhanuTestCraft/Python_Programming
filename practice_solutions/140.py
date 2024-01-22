"""
Write a program that accepts a string and capitalizes the first letter of each word while converting all other letters to lowercase.
input: "heLLo WORLD"
output: Hello World
"""
my_string = "heLLo WORLD"
# my_string = my_string.capitalize()
# print(my_string)
my_list = my_string.split()
new_string = " ".join(i.capitalize() for i in my_list)
print(new_string)
