marks = [12, 56, 48, 98, 45, 1, 4]

# method-1:
# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Awesome !!")
#     index += 1

# method-2:
# for index, mark in enumerate(marks):
#     print(mark)
#     if index == 3:
#         print("Awesome !!")

for index, mark in enumerate(marks):
    print(index, mark)
# output:
# 0 12
# 1 56
# 2 48
# 3 98
# 4 45
# 5 1
# 6 4
# Here we can see the default counter is starting from the 0 but we can modify the count value by passing start argument to enum function.

for index, mark in enumerate(marks, start=1):
    print(index, mark)
# output:
# 1 12
# 2 56
# 3 48
# 4 98
# 5 45
# 6 1
# 7 4
