# Functions are something pre-defined which have some inbuilt logic and when we call that function it will internally run all the lines written in that function internally and return the output

# When we use specific functions to the list they are kniwn as methods.
# print(len(a))
# print(sum(a))
# print(max(a))
# print(min(a))

# Mutable/Immutable data type.
# In case of mutable data type we can update the data while in case immutable data type once created can't be updated.


a = [54, 23, 10, 99, -90]
print(a)

# append: is used to insert any value in the list at the last index.
# a.append(100)
# a.append("Bhanu")
# a.append("sheetal")
# a.append(87)

# insert: is used to add any value at desired index.
# a.insert(2, "Python")

# Updating the list.
# a[0] = 100
# a[-1] = 100
# This is the classic example where we are able to update the list so it is mutable.

# Deleting any element from the list
# If nothing is provided in argument it will pop last value.
# a.pop()
# if we give value in argument it will pop that index element.
# a.pop(0) #remove by index.
# a.remove(10)  # remove by value.
# del a[0] #can be used for any data type.

# clear : is used to remove all the values from the list.
a.clear()
print(a)
