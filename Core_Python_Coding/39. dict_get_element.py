my_dict = {
    "name": "Bhanu",
    "age": 27,
    "gender": "male",
}

# There is no position/index in the dictionary.

# To get value
# r = my_dict.get("name")
# print(f"my name is {r}")
# print(my_dict)

k = input("Enter any key = ")
result = my_dict.get(k)
if result is not None:
    print(result)
else:
    print("Key does not exist")

# print(f'my name is {my_dict["name"]}')
# print(f'my age is {my_dict["age"]}')
# print(f'my gender is {my_dict["gender"]}')
