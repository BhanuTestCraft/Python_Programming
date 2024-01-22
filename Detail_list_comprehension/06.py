# Dictionary comprehension in python.
age_dict={
    "jack":38,
    "michael":48,
    "guido":57,
    "john":33
}
result = {k:v*2 for k,v in age_dict.items()}
print(result)
# output: {'jack': 76, 'michael': 96, 'guido': 114, 'john': 66}
# Here the age for user got modified using the dictionary comprehension.

result={i: chr(65+i) for i in range(4)}
print(result)
# output: {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

result={i:i**2 for i in range(5)}
print(result)

result={i:str(i) for i in range(5)}
print(result)

# maping of two list into the dictionary using dictionary comprehension.
fruit_no=["fruit1","fruit2","fruit3","fruit4"]
fruit=["Apples","Pears","Mango","Bannana"]
result={fruit_no[i]:fruit[i] for i in range(len(fruit_no))}
print(result)

result={}
for i in fruit_no:
    for p,j in enumerate(fruit):
        if i not in result:
          result[i]=j
          fruit.pop(p)
print(result)

result={k.capitalize() for k in age_dict.keys()}
print(result)
# output: {'Michael', 'Jack', 'Guido', 'John'}

result={v for v in age_dict.values()}
print(result)
# output: [48, 57, 38, 33]

result={k:v for k,v in age_dict.items() if v>40}
print(result)

# if else with the dictionary comprehension
# syntax: result={(k if else):(v if else) for k,v in age_dict.items()}
result={k:("old" if v>40 else "young") for k,v in age_dict.items()}
print(result)