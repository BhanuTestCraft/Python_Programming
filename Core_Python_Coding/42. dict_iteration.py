my_dict = {
    "name": "Bhanu",
    "age": 27,
    "gender": "male",
}
# To print the keys.
for k in my_dict.keys():
    print(k)

# To print the values.
for k in my_dict.keys():
    print(my_dict[k])

for v in my_dict.values():
    print(v)

# To print the key and values.
for k in my_dict.keys():
    print(f"{k} -> {my_dict.get(k)}")

for k, v in my_dict.items():
    print(f"{k} -> {v}")
