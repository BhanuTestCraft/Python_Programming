# write the python program to find the number of digits in the given number.
num=int(input("Enter the value of number: ") )
def digit_count(num):
    if num<10:
        return 1
    return 1+digit_count(num//10)

result= digit_count(num)
print(f"Number of digits in the given number is {result}")