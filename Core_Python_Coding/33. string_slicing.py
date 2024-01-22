a = "code and debug"
b = a[0:4]
print(b)

b = a[0:]
print(b)

b = a[len(a) :: -1]
print(b)

b = a[-5:]
print(b)

# Check if a string is palindrome or not
# mom---mom
# abc---cba
# noon--noon
my_string = input("Enter the string= ")
rev_string = my_string[::-1]
if my_string == rev_string:
    print(f"given string {my_string} is palindrome")
else:
    print(f"given string {my_string} is not a palindrome")
