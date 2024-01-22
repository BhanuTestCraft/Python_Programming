# Data Type: data type specifies which type of value a variable has and what mathematical,relational,or logical operations can be performed on it without causing an error.

"""
Differenet data types available in python are as follows:
1. Numeric Type: Integers,float,complex.
2. Dictionary
3. sequence Type: List,Tuple,Strings.
4. Set
5. Boolean: True, False
"""

"""
List: To store the multiple values in single varaible
Lists are different from the arrays as in array we can store the single data types while in the lists we can store values of any data type.
my_list=[55,78.5,"Bhanu",True]--->Here in the list we can update the list later on after the declaration i.e lists are mutable
"""

"""
Tuple: is same as list but have slight diff that it will not get updated once declared i.e immutable
my_tuple=(55,78.5,"Bhanu",True)
"""

"""
Dictionary: values are stores as a pair of key-value
my_dict={"name":"Anirudh","marks":90}
"""

# Integer data type.
x=25
print(x)
print(type(x)) #type() is an inbuilt function to determine the data type of the variable.

# Float data type.
y=90.5
print(y,type(y))

# String data type.
name="Bhanu Pratap"
print(name,type(name))

# Boolena data type.
condition=True
print(condition,type(condition))

# List data type.
my_list=[10,20,30,40]
print(my_list,type(my_list))

# Tuple data type.
my_tuple=(15,25,35,45)
print(my_tuple,type(my_tuple))

# Dictionary data type.
my_marks_dict={"Bhanu":99,"Sheetal":100}
print(my_marks_dict,type(my_marks_dict))