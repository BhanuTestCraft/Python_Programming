# write a python program for printing n to 1 sequence.

num=int(input("Enter the value of n: "))

def sequence(num):
    print(num,end=" ")
    if num==1:
        return
    return sequence(num-1)

sequence(num)