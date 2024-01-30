# Merging two dictionaries.
# Input: {'a': 1, 'b': 2}, {'c': 3, 'd': 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
def merge_dicts(dict1,dict2):
    merged_dict={}
    for key,value in dict1.items():
        merged_dict[key]=value
    for key,value in dict2.items():
        merged_dict[key]=value
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dicts(dict1,dict2)
print(f"The dictionary after the merging is {result}")

def merge_dicts(dict1,dict2):
    merged_dict = {key:value for key,value in dict1.items()}
    merged_dict.update({key:value for key,value in dict2.items()})
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dicts(dict1,dict2)
print(f"The dictionary after the merging is {result}")
    