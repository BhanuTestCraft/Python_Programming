# list comprehension vs Generator expression.
result=[i for i in range(100)]
print(result)

result=(i for i in range(100))
print(result)
# it will reyurn a generator object
# output: <generator object <genexpr> at 0x100a5c790>
# We can wrap this expression in desired data type as trhe output.

result=list((i for i in range(100)))
print(result)

import sys
sys.stdout.write("Hey we are learning list comprehension\n")
sys.stdout.write("Generator expression")
a=[i for i in range(100)]
print(a)
b=(i for i in range(100))
print(b)
print(sys.getsizeof(a))
# output: 920
print(sys.getsizeof(b))
# output: 200
# i.e it is taking much less space in the memory as compared to the list comprehension.

a=[i for i in range(1000)]
print(a)
b=(i for i in range(1000))
print(b)
print(sys.getsizeof(a))
# output: 8856
print(sys.getsizeof(b))
# output: 200
# we can observe that for the list comprehension we can see size increases by the 10 times but for the generator expression it is still the same.that's why geneartor expression are quite faster.

# To calculate the time for both expressions in order to know the execution time of both the expression.
from timeit import timeit
result=timeit("[i for i in range(100)]")
print(result)
# time: 1.1419274999934714
result=timeit("(i for i in range(100))")
print(result)
# time: 0.19219383399467915


result=timeit("[i for i in range(1000)]")
print(result)
# time: 12.251305709010921
result=timeit("(i for i in range(1000))")
print(result)
# time: 0.20937500000582077
# Therefore it is better to use the geneartor expression as compared to list comprehension.

# when we want to access the method used for the list we first need to wrap the generator expression with the list.
a=(i for i in range(10))
print(a)
list(a).append(11)
print(a)

b=list(i for i in range(10))
print(b)
print(b[3])