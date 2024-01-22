"""
Ask a string from user. Count the number of uppercase and lowercase characters in that String.
"""
my_str = "abc123ABCD"
lower_count = 0
upper_count = 0
# Method-1
# for ch in my_str:
#     if ch.islower():
#         lower_count += 1
#     elif ch.isupper():
#         upper_count += 1

# Method-2
for ch in my_str:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        upper_count += 1
    elif ascii >= 97 and ascii <= 122:
        lower_count += 1

print(f"No of lower case letter are {lower_count}")
print(f"No of upper case letter are {upper_count}")
