# Count

my_string = "Hello World"
result = my_string.count("H")
print(result)  # output:1

result = my_string.count("h")
print(result)  # output:0

result = my_string.count("ll")
print(result)  # output:1

# Index

result = my_string.index("H")
print(result)  # output:0

# result = my_string.index("h")
# print(result)  # output:ValueError: substring not found


# find
result = my_string.find("H")
print(result)  # output:0

result = my_string.find("h")
print(result)  # output:-1
# In find method if we do not find the char in string we will get output as -1.

# replace
result = my_string.replace("l", "z")
print(result)  # output:Hezzo Worzd

# strip: Removes all the blank sapces before and after in the string.
str = "    Hello World    "
str1 = "@@@@Hello World@@@@"
result = str.strip()
result1 = str1.strip("@")
print(str)
print(result)
print(str1)
print(result1)
