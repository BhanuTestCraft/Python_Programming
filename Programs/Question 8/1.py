"""
Python Program to Print all Prime numbers in an Interval
"""
start_num = int(input("Enter the starting number = "))
end_num = int(input("Enter the ending number = "))
my_list = []
for i in range(start_num, end_num + 1):
    my_list.append(i)
print(f"List of all number is range= {my_list}")
prime_list = []
factors = 0
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        prime_list.append(num)

print(f"Numbers that are prime is there in list = {prime_list}")
