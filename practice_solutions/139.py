"""
Write a program to reverse the order of words.
input: "Hello world"
output: world Hello
"""
my_string = "Hello world"
print(my_string)
my_list = my_string.split()
# method:1
# print(my_list)
# for i in range(len(my_list) - 1, -1, -1):
#     print(my_list[i], end=" ")

# method:2
# new_list = []
# for i in range(len(my_list) - 1, -1, -1):
#     new_list.append(my_list[i])
# reverse_string = " ".join(new_list)

# method:3
my_list = my_list[::-1]
reverse_string = " ".join(my_list)
print(reverse_string)
