# Python | Sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

input_list = [12, 67, 98, 34]
output_list = []
for value in input_list:
    sum=0
    for digit in str(value):
        sum+=int(digit)
    output_list.append(sum)
print(output_list)
