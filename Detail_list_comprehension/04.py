# list comprehension vs map function.
list1=[1,2,3,4]
result=[i*2 for i in list1]
print(result)

# using map function
def multipleTwo(num):
    return num*2
result=list(map(multipleTwo,list1))
result1=list(map(lambda x:x*2,list1))
print(result)
print(result1)

# use of map and filter together
result=[i for i in list1 if i>2]
print(result)
# output: [3, 4]
result=list(map(lambda x: x ,list1))
print(result)
# output: [1,2,3,4]
result1=list(map(lambda x: x,filter(lambda x:x>2,list1)))
print(result1)

# we can use the map function with the pre-defined function as compared to the lambda as it will take the less time.
from timeit import timeit
print(timeit("map(multipleTwo,[1,2,3,4])", "from __main__ import multipleTwo"))
# Time: 0.07635062500776257
print(timeit("map(lambda x:x*2,[1,2,3,4])", "from __main__ import multipleTwo"))
# Time: 0.1075817079981789
# Therefore it require more time to perform the operation when we use the lamda with map function instead of the pre-defined function.

print(timeit("[i*2 for i in [1,2,3,4]]", "from __main__ import multipleTwo"))
# Time: 0.15449266700306907
# Therefore the list comprehension will take even more time compared to the lamda in map.

print(timeit("[multipleTwo(i) for i in [1,2,3,4]]", "from __main__ import multipleTwo"))
# Time: 0.23547887499444187

# Final conclusion is that if we are working with the small numbers we can use the map with pre-defined function and that will be quicker as compared to the list comprehension
# While when we will be working with the large number we can say list comprehension will be the faster as compared to the map function.
