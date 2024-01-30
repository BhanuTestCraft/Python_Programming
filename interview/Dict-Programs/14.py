# Checking if a key exists in a dictionary:
# Input Dictionary: {'a': 1, 'b': 2, 'c': 3}
# Key to check: 'b'
# Output: True

def is_key_there(dict,key):
    for k in dict:
        if k==key:
            return True
    return False

dict = {'a': 1, 'b': 2, 'c': 3}
k = 'd'
result = is_key_there(dict,k)
print(f"The key {k} is there in dict : {result}")