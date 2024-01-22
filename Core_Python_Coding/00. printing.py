name = "Anirudh"
age = 18

# Method 1:
print("My name is", name)
print("My age is", age)
print("My name is", name, "and age is", age)

# Method 2: using identifiers
print("My name is %s and my age is %d" % (name, age))
# Here our name is a string so we used %s and since our age is intger type so we use %d.
# %s refers to a string data type, %f refers to a float data type, and %d refers to a double data type.

# Method 3: using f string
print(f"My name is {name}")
print(f"My age  is {age}")
