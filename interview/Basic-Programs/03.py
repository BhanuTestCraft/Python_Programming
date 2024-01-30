# Python Program to Print all Prime numbers in an Interval.
def prime(x,y):
    my_list = [i for i in range(x,y+1)]
    prime_list = []
    for num in my_list:
        factors = 0
        for i in range(1,num+1):
            if num%i==0:
                factors+=1
        if factors == 2:
            prime_list.append(num)
    return prime_list
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
result = prime(start,end)
print(f"All the prime no's in the range are {result}")

def prime(start,end):
    list =[]
    for i in range(start,end+1):
        factors = 0
        for j in range(1,i+1):
            if i%j==0:
                factors+=1
        if factors ==2:
            list.append(i)
    return list
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
result = prime(start,end)
print(f"All the prime no's in the range are {result}")