# enumerate with the list comprehension
fruits=["Apples","Mango","Pears","Bannana"]
for i,v in enumerate(fruits):
    print(f"{i}-->{v}")

result=[i for i in enumerate(fruits)]
print(result)
# output : [(0, 'Apples'), (1, 'Mango'), (2, 'Pears'), (3, 'Bannana')]

result=[(i,v) for i,v in enumerate(fruits)]
print(result)
# output: [(0, 'Apples'), (1, 'Mango'), (2, 'Pears'), (3, 'Bannana')]

result=[{i:v} for i,v in enumerate(fruits)]
print(result)
# output: [{0: 'Apples'}, {1: 'Mango'}, {2: 'Pears'}, {3: 'Bannana'}]

result=[i for i,v in enumerate(fruits)]
print(result)
# output: [0, 1, 2, 3]

result=[v for i,v in enumerate(fruits)]
print(result)
# output: ['Apples', 'Mango', 'Pears', 'Bannana']

result={i:v for i,v in enumerate(fruits)}
print(result)
# output: {0: 'Apples', 1: 'Mango', 2: 'Pears', 3: 'Bannana'}