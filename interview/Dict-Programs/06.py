# Python – Insertion at the beginning in OrderedDict.
# Input: 
# original_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)

# Output:  {'c':3, 'a':1, 'b':2}

input_dict = {'a':1, 'b':2}
# item to be inserted ('c', 3)
empty_dict = {}
empty_dict.update({'c':3})
print(empty_dict)
empty_dict.update(input_dict.items())
print(empty_dict)