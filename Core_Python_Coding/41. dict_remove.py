my_dict = {
    "name": "Bhanu",
    "age": 27,
    "gender": "male",
}

print(my_dict)

# method:1
del my_dict["gender"]
print(my_dict)

# method:2
my_dict.pop("age")
my_dict.popitem()  # It will empty the entire dict.
print(my_dict)
