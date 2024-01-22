# Even - return True
# Odd - return False

check_even = lambda num: num % 2 == 0

n = int(input("Enter any number= "))
if check_even(n):
    print("Even")
else:
    print("Odd")
