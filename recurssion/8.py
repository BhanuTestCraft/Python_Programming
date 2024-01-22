# write a python program for fibonacci series using the recurssion.
def fib_series(num):
    if num==1:
        return 0
    if num==2:
        return 1
    return (fib_series(num-2)+fib_series(num-1))

num=int(input("Enter the value of number: "))
for i in range(1,num+1):
    print(fib_series(i),end=" ")