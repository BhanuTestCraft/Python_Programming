my_dict = {
    "name": "Bhanu",
    "age": 27,
    "gender": "male",
}
print(my_dict)
# Method:1
my_dict["age"] = 28
my_dict["contact"] = 91
# if key is not existing already it will create the key in dictionary else update the existing key.(Add/Update)
print(my_dict)

# Method:2
my_dict.update({"marks": 89, "address": "Delhi"})
print(my_dict)
