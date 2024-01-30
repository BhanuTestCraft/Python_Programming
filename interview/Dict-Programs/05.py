# Python – Convert key-values list to flat dictionary.
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
def flat_dict(test_dict):
    dict = {}
    for i in range(len(test_dict["month"])):
        dict[test_dict["month"][i]] = test_dict["name"][i]
    return dict
result = flat_dict(test_dict)
print(f"dict after flattening is {result}")

test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}

result = dict(zip(test_dict["month"],test_dict["name"]))
print(f"dict after flattening is {result}")