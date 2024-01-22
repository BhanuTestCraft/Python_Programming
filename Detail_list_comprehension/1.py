# With integers in the list.
nums=[1,2,3,4]

# method:1
result=[]
for i in nums:
    i=i*2
    result.append(i)
print(result)

# method:2
result=[i*2 for i in nums]
print(result)

# With strings
strings=["intro","to","list","comps"]

# method:1
result=[]
for i in strings:
    i=i.upper()
    result.append(i)
print(result)

# method:2
result=[i.upper() for i in strings]
print(result)

def TimeFive(num):
    return num*5

# method:1
result=[]
for i in nums:
    i=TimeFive(i)
    result.append(i)
print(result)

# method:2
result=[TimeFive(i) for i in nums]
print(result)
# That concludes us that we can also use the functions inside the list comprehension.

# list of dictionary.
dict=[{"name":"Bhanu"},{"name":"tushar"}]

# grab the names out of dict
result=[]
for element in dict:
    result.append(element["name"])
print(result)

# method:2
result=[i["name"] for i in dict]
print(result)
