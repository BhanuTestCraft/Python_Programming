""" Identity operator: 
1. They will compare the id's(memory address) of the objects.
2. Used to know two objects are same or not.

-----------
Types:
1. is
2. is not
"""
a=100
b=100
print(id(a)) # mem_addr: 4317032344
print(id(b)) # mem_addr: 4317032344
# That means python allocate the sam memory to both and we are having two tags to access this particular address.
result= a is b # id(a)==id(b)
print(result)
c="Bhanu"
# Here c is allocated some different memory location.
print(id(c))
result1= c is a
print(result1)

"""
Difference between is operator amnd == operator.
1. Firstly is an special operator in python while == operator is comparison operator in the python.
"""
a=100
print(f"Id/memory loaction of variable a is: {id(a)}")

b=100
print(f"Id/memory loaction of variable b is: {id(b)}")

print(a==b) # 100==100---> True as the output.
# Here the value assigned 100 is compared.

# ------------------------------------------------
print(a is b) # id(a)==id(b)-->True as the output.
# Here the id for the value is getting compared i.e memory location for these a and b.

# ------------------------------------------------
a=[10,20,30,40]
print(f"Id for the list a is : {id(a)}")
# output: Id for the list a is : 4365751616

b=[10,20,30,40]
print(f"Id for the list b is : {id(b)}")
# output: Id for the list b is : 4365944192
# Note: Here we will see that memory allocation for both the list will be the different because list is a mutable object and that can change it's value anytime of the execution.

print(a is b) # id(a)==id(b)--->False
print(a==b) # a==b--->True