"""
Make your own list. Print all the elements present at even index position.
"""
# Iteration by the position/Index.
my_list = [51, 74, 25, 66, 91, 88]
for i in range(0, len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")
