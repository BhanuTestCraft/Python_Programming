list1=[1,2,3]
result=[i*5 if i==3 else i for i in list1]
print(result)
# output: [1, 2, 15]

# If else written before the for loop are used to get the desired result and if condition return after the for loop is used to filter the data.

result=[i*5 if i==3 else i for i in list1 if i==3]
print(result)
# output: [15]
# Here we are using a filter condtion on the right of the loop and that is the reason the outputs are different.
# Also you cant have the else on to the right if the for loop because in case of the filter there is no else in that and that will lead to the invalid syntax.
# If we are writing any filter on to the left of the for loop then we need to have the if and else both statement while on the right there will be no else.

result=list(map(lambda i: i*5 if i==3 else i,list1))
print(result)
# output: [1, 2, 15]
# Now to filter the desired output we can pass the filtered list in place of the list1 as shown below.
result=list(map(lambda i: i*5 if i==3 else i,filter(lambda i: i>1,list1)))
print(result)
# output: [2, 15]

result=[]
for i in list1:
    if i==3:
        result.append(i*5)
    else:
        result.append(i)
print(result)
# output=[1,2,15]

# using filter in the above loop
result=[]
for i in list1:
    if i==3:
        result.append(i*5)
    else:
        if i>1:
         result.append(i)
print(result)
# output: [2, 15]