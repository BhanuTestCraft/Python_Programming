"""
Print the following pattern.
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
# When we are seeing same numbers while print then we need to print i else we need to print j.
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(i, end=" ")
    print()
