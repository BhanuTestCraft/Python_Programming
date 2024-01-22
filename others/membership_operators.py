"""
Basically there are two type of operators in python:
1. membership operator.
2. identity operator.
why there are so special:
1. other programming languages like c,c++,java do not have these operators.
2. These operators firstly inroduced in the python.
3. Perl,wift,PHP developed afte the python coped these opertaors.

--------------------
Need of these operators:
These operators are mostly used with the sequences like list,tuple,string and the dictionary.
"""

whatsapp_group=["Aman","Raj","Jay","Chutki"]
# To check the member of the list i.e membership operator.
result = "Jay" in whatsapp_group
print(result,type(result))

"""
Membership operator:
1. Check the existence of any value in the sequence or in the layemen language we can say that check the value is the member of the sequence or not.
2. Sequence can be list,string,tuple,dictionary.
-----
Types:
1. in
# It will return the output as True when the particular element is present in the given sequence else it will return false.
2. Not in
#  It will return the output as True when the particular element is not present in the given sequence elese it will return False.
"""
my_str="Shantanu"
result="tanu" in my_str
print(result,type(result))

list=[10,20,30,40,50]
result=20 in list
result1=100 not in list
print(result,type(result))
print(result1,type(result1))

# Memebership operator working in the dictionary.
my_dict={1:"Bhanu",2:"Tushar"}
# When we use the menbership operator in here it will check the value with the key not with the value corresponding to the key.
result= "Bhanu" in my_dict
# Here we are checking the value in the dict which is not supported.
result1= 1 in my_dict
# Here we are checking the key in the dict or not which will work properly.
print(result)
# output: False
print(result1)
# output: True