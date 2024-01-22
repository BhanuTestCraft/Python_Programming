# list comprehnsion with multiple if statements.
list=[1,2,3,4,5]
result=[i for i in list if i>2 if i!=8]
print(result)
# output: [3, 4, 5]

# 1
result=[i for i in list if i>2]
print(result)
# if done with loop
result=[]
for i in list:
    if i>2:
        result.append(i)
print(result)

# 2
result=[i for i in list if i>2 if i!=3]
print(result)
# using the loop
result=[]
for i in list:
    if i>2:
        if i!=3:
         result.append(i)
print(result)

# 3
result=[i for i in list if i>2 and i!=3]
print(result)
# using the loop
result=[]
for i in list:
   if i>2 and i!=3:
      result.append(i)
print(result)

fruit=["Apples","Peaches","Pears","Bananas"]
result=[(i,f) for i in list if i>2 for f in fruit]
print(result)
# using loop
result=[]
for i in list:
   if i>2:
      for f in fruit:
       result.append((i,f))
print(result)

# using multiple filters in the list comp
result=[(i,f) for i in list if i>2 if i!=3 for f in fruit]
print(result)
# using the loops
result=[]
for i in list:
   if i>2:
      if i!=3:
         for f in fruit:
            result.append((i,f))
print(result)

# use another if with the fruits
result=[(i,f) for i in list if i>2 if i!=3 for f in fruit if f!="Pears"]
print(result)
# using the loops
result=[]
for i in list:
   if i>2:
      if i!=3:
         for f in fruit:
            if f!="Pears":
               result.append((i,f))
print(result)

# using more and condition in fruit
result=[(i,f) for i in list if i>2 if i!=3 for f in fruit if f!="Pears" and f!="Apples"]
print(result)
# using the loops
result=[]
for i in list:
   if i>2:
      if i!=3:
         for f in fruit:
            if f!="Pears" and f!="Apples":
               result.append((i,f))
print(result)

# using multiple if statement in fruit
result=[(i,f) for i in list if i>2 if i!=3 for f in fruit if f!="Pears" if f!="Apples"]
print(result)
# using loops
result=[]
for i in list:
   if i>2:
      if i!=3:
         for f in fruit:
            if f!="Pears":
               if f!="Apples":
                  result.append((i,f))
print(result)