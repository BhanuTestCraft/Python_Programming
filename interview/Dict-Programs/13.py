# Finding the key with the maximum value in a dictionary.
# Input: {'a': 10, 'b': 5, 'c': 8}
# Output: 'a'

def max_key(dict):
    max_key = None
    max_value = float("-inf")
    for key,value in dict.items():
        if value>max_value:
            max_value=value
            max_key=key
    return max_key
dict = {'a': 10, 'b': 5, 'c': 8}
result = max_key(dict)
print(type(result))
print(f"The key with max value is {result}")