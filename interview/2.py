# Write a python program to move all the even numbers to the front of the list while maintaing the orignal order. The odd numbers should follow the orignal order.
my_list=[1,2,3,4,5,6,7,8,9]

# Method 1:
# new_list=[]
# for value in my_list:
#     if value%2==0:
#         new_list.append(value)
# for value in my_list:
#     if value%2!=0:
#         new_list.append(value)
# print(new_list)

# Method 2:
# even=[]
# odd=[]
# def solution(my_list):
#     for value in my_list:
#         if value%2==0:
#             even.append(value)
#         else:
#             odd.append(value)
#         return even+odd

# result = solution(my_list)
# print(result)

# Method 3: using the list comprehension.
def solution(my_list):
    even=[i for i in my_list if i%2==0]
    odd=[i for i in my_list if i%2!=0]
    return even+odd

result = solution(my_list)
print(result)