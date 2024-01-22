a = [55, 65, -95, "Bhanu", 55.6, -95, "code"]
# Since list is mutable data type so it is not prefered to copy like this because what python does that it assign the same address of first value to both a and b in memory so now if we update anything in a it will automatically update same in b.
# b=a
# print(a)
# print(id(a))
# print(b)
# print(id(b))

# a[2]=100
# print(a)
# print(b)

# To overcome this issue we use one function copy.
b = a.copy
print(id(a))
print(id(b))
