"""
membership operator: If we need to check that any value exist or not in the sequence i.e list,string,tuple,dict etc.
types:
1. in
2. not in
"""
a = [55, 65, -95, "Bhanu", 55.6, -95, "code"]
# print("Bhanu" in a)
# print(1000 in a)
# print(1000 not in a)
# print("code" in a)

# Ask a number from the user.
# print yes if number in list else print no.
num = int(input("Enter the value of number= "))
if num in a:
    print("Yes")
else:
    print("No")
