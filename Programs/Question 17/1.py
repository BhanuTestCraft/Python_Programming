# function to rotate array by d elements using temp array
my_list = [1, 2, 3, 4, 5, 6, 7]

# implementing using the list slicing.
c = my_list[2:] + my_list[:2]
print(f"Array after left rotation is: {c}")


# rotate the array left by 2 unit.
temp_list = [1, 2]
new_list = []
for i in range(len(temp_list), len(my_list)):
    new_list.append(my_list[i])

result = new_list + temp_list
print(f"Array after left rotation is: {result}")


# implementing using the function.
def rotate_array(arr, r, l):
    """Here arr is the array we need to rotate, r is the no of unit by which we need to rotate it left and l is the length of array"""
    temp_list = []
    i = 0
    while i < r:
        temp_list.append(arr[i])
        i += 1
    i = 0
    while r < l:
        arr[i] = arr[r]
        i += 1
        r += 1
    arr[:] = arr[:i] + temp_list
    return arr[:]


print(f"Array after left rotation is: {rotate_array([1, 2, 3, 4, 5, 6, 7], 2, 7)}")
