# Python program to find the sum of all items in a dictionary.
# Input : {‘a’: 100, ‘b’:200, ‘c’:300}
# Output : 600

test_dict = {"a": 100, "b":200, "c":300}
def sum(dict):
    total = 0
    for value in dict.values():
        total+=value
    return total

result = sum(test_dict)
print(f"sum of all the value in given dict is {result}")