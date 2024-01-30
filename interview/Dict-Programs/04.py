# Python | Merging two Dictionaries.
# Input: 
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# Output: {'a': 10, 'b': 8, 'd': 6, 'c': 4}

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
merge_dict = {}

for key,value in dict1.items():
    merge_dict[key]=value
for key,value in dict2.items():
    merge_dict[key]=value
print(merge_dict)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
merge_dict = {}
merge_dict = {key:val for key,val in dict1.items()}
merge_dict.update({key:val for key,val in dict2.items()})
print(merge_dict)