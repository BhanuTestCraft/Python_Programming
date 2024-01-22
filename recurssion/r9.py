# Write the python program to find the sum of first n natural number.

n=int(input("Enter the value of n: "))

# def sum(n,i):
#     if i==n:
#         return i
#     return i+sum(n,i+1)

# result=sum(n,i=1)
# print(result)

def sum(n,i):
    if i==1:
        return 1
    return i+sum(n,i-1)

result=sum(n,n)
print(f"Sum first {n} natural numbers is {result}")