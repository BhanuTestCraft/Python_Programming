"""
Write a program that reverses each word in a sentence while maintaining the word order. For example, "Hello World" should become "olleH dlroW"
"""
my_string = "Hello World"
my_list = my_string.split()
result = " ".join(i[::-1] for i in my_list)
print(result)
