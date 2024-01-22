# printing list comprehension in python
result= [print(i) for i in range(5)]
# output: 0 1 2 3 4
print(result)
# actually print function does not return anything and the function which does not return anything is equivalent to the none.

def printVal(val):
    print("val:", val)
result=[printVal(i) for i in range(5)]
print(result)
# output: 
# val: 0
# val: 1
# val: 2
# val: 3
# val: 4
# [None, None, None, None, None]

# method:1
def printReturnVal(val):
    print("val:",val)
    return val
result=[printReturnVal(i) for i in range(5)]
print(result)
# output:
# val: 0
# val: 1
# val: 2
# val: 3
# val: 4
# [0, 1, 2, 3, 4]

# method:2
print([i for i in range(5)])

# method:3
result = [print(i) or i for i in range(5)]
print(result)
# Best method to print in the list comprehension.

result=[print(i) or str(i) for i in range(5)]
print(result)