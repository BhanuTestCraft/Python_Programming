"""
Uses of eval function:
1. To solve the mathematical expression present in the string.
2. To take the user inputs like list,dict,tuple etc.
"""

num=3
var=eval("num*num")
# argument for the eval function must be a string.
print(var,type(var))

# Let us assume we want to take the list input from the user:
my_list=eval(input("Enter the list here: "))
print(my_list,type(my_list))
# Enter the list here: [1,2,3,4]
# [1, 2, 3, 4] <class 'list'>
# That's how we can take inputs of the list, tuple, dictionary etc.. from the user.
