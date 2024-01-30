# Python – Append Dictionary Keys and Values ( In order ) in dictionary.
# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3} 
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3] 
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
def fun(test_dict):
    list = []
    for key in test_dict.keys():
       list.append(key)
    for value in test_dict.values():
       list.append(value)
    return list
result = fun(test_dict)
print(result)

def fun(test_dict):
   list1 = [i for i in test_dict.keys()]
   list2 = [i for i in test_dict.values()]
   list = list1 + list2
   return list
result = fun(test_dict)
print(result)