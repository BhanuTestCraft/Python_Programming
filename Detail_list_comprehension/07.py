# list comprehension with multiple for loops
nums=[1,2,3,4]
fruits=["Peaches","Pears","Mango","Apples"]
result=[(i,f) for i in nums for f in fruits]
print(result)
# result can be list of any data type i.e list of list, list of tuple, list of dictionary
result1=[{i:f} for i in nums for f in fruits]
print(result1)
result2=[[i,f] for i in nums for f in fruits]
print(result2)

# using loop
result=[]
for i in nums:
    for f in fruits:
        result.append((i,f))
print(result)

# Most important use of the multiple for loops in the list comprehension is the faltenning of the list
list1=[[1,2,3],[10,20,30],[65,78]]
result=[item for sublist in list1 for item in sublist]
print(result)
# output: [1, 2, 3, 10, 20, 30, 65, 78]