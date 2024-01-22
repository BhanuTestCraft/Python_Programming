"""
Join: converts a list into the string.
"""
my_list = ["Hello", "world", "this", "is", "python"]
my_string = " ".join(my_list)
print(my_string, type(my_string))
# output:Hello world this is python <class 'str'>


my_list = ["Hello", "world", "this", "is", "python"]
my_string = "-".join(my_list)
print(my_string, type(my_string))
# output:Hello-world-this-is-python <class 'str'>


# my_list = ["Hello", "world", "this", "is", "python", 87]
# my_string = " ".join(my_list)
# print(my_string, type(my_string))
# output: TypeError: sequence item 5: expected str instance, int found


my_list = ["Hello", "world", "this", "is", "python", 87]
my_string = " ".join(str(i) for i in my_list)
print(my_string, type(my_string))
# output:Hello world this is python 87 <class 'str'>

my_list = ["Hello", "world", "this", "is", "python", 87]
my_string = " ".join(str(i)[::-1] for i in my_list)
print(my_string, type(my_string))
# output:olleH dlrow siht si nohtyp 78 <class 'str'>
