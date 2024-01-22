# list comprehension vs filter() function.
from timeit import timeit
list1=[1,2,3,4,5]
result=[i for i in list1 if i>2]
print(result)
t1=timeit("[i for i in [1,2,3,4] if i>2]")
print(t1)
# output: t1: 0.12826912499440368

# using the filter
def fun(num):
    if num>2:
        return num

result=list(filter(fun,list1))
print(result)
t2=timeit("list(filter(fun,[1,2,3,4]))", "from __main__ import fun")
print(t2)
# output: t2: 0.19791995800915174
result=list(filter(lambda x: x>2,list1))
print(result)
t3=timeit("list(filter(lambda x: x>2,[1,2,3,4]))")
print(t3)
# output: t3: 0.23393650000798516

# use of None in filter
result=list(filter(None,[0,0,1,2,3,False,True,False]))
print(result)
# output: [1, 2, 3, True]
# This none as default argument will filter anything which is False.

