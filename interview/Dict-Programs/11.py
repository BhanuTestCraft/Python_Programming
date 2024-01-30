# Counting occurrences of elements in a list using a dictionary:.
# Input: ['apple', 'banana', 'apple', 'orange', 'banana']
# Output: {'apple': 2, 'banana': 2, 'orange': 1}
list = ['apple', 'banana', 'apple', 'orange', 'banana']
output = {}
for value in list:
    if value in output.keys():
        output[value]+=1
    else:
        output[value] = 1

print(output)