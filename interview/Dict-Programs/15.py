# Converting a list of dictionaries into a dictionary of lists.
# Input: [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
# Output: {'a': [1, 3, 5], 'b': [2, 4, 6]}

input_list = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
dict = {}
for ele in input_list:
    for key,value in ele.items():
        if key in dict.keys():
            dict[key].append(value)
        else:
            dict[key] = [value]

print(dict)

