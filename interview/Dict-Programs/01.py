# Python – Extract Unique values dictionary values.
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
out_list = []
for value in test_dict.values():
    for i in value:
        if i not in out_list:
            out_list.append(i)

out_list.sort()
print(out_list)


test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
def unique_dict(dict):
    out_list = []
    for value in dict.values():
        for i in value:
            if i not in out_list:
                out_list.append(i)
    out_list.sort()
    return out_list
print(unique_dict(test_dict))
