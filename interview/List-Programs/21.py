# Python | Count occurrences of an element in a list
my_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
def count_number(num,my_list):
    count = 0
    for value in my_list:
        if value == num:
            count+=1
    return count
num  = int(input("Enter the number = "))
result = count_number(num,my_list)
print(f"number {num} occured {result} times.")

my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
def count_number(num,list):
    new_list = [i for i in list if i==num]
    return len(new_list)
result = count_number(2,my_list)
print(f"number 2 occured {result} times.")