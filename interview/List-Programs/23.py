# Python program to find Cumulative sum of a list.
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]

input_list = [10, 20, 30, 40, 50]
def cummulative_sum(list):
    new_list = []
    total = 0
    for value in input_list:
        total+=value
        new_list.append(total)
    return new_list
result = cummulative_sum(input_list)
print(f"The list with cummulative sum is : {result}")

