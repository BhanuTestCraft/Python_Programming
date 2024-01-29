# Python Program to Swap Two Elements in a List.
my_list=[1,2,3,4,5]
def swapElement(my_list: list) -> list:
    # let us assume we need to swap the two elements i.e pos1 and pos2 which will be given by the user.
    pos1=int(input("Enter the position for first element: "))
    pos2=int(input("Enter the position for second element: "))
    temp=my_list[pos1]
    my_list[pos1]=my_list[pos2]
    my_list[pos2]=temp
    return my_list

result = swapElement(my_list)
print(f"The list after swapping desired elements is : {result}")