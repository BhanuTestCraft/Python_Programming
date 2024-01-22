"""
Title,capitalized,upper,lower,swapcase
isupper,islower,isalpha,isalnum,isspace
"""
# Title method.
# It will capitalise every first letter present in the string input.
a = "anirudh"
b = "bhanu code and debug"
x = a.title()
y = b.title()
print(x)
print(y)

# Capitalized method
# it will only capitalize the first letter of string not in each word.
z = b.capitalize()
print(z)

# upper method.
# It will convert each letter in string to capital letter.
p = b.upper()
print(p)

# lower method.
# It will convert each letter of string into lower case.
str = "BHANU"
m = str.lower()
print(m)

#  isupper method.
my_str = "bhanu Pratap Code and DEBUG"
str = "BHANU"
str1 = "bhanu"
str2 = "bhanupratap"
str3 = "bhanu1pratap2"
s = my_str.isupper()
s1 = str.isupper()

# islower method
s2 = my_str.islower()
s3 = str1.islower()

# isalpha method
s4 = (
    my_str.isalpha()
)  # output:False because entire string should have only the aplhabets anb even the space is not allowed.
s5 = str2.isalpha()

# isalnum method
s6 = str3.isalnum()

print(s)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

a = "1234"
if a.isdigit():
    a = int(a)
    print(a, type(a))
else:
    print("cannot be converted to integer.")
