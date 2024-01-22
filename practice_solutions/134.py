"""
Ask a string from user. Convert all the alphabets to uppercase
"""
my_str = "abc123ABCD"

# Method 1:
# result = my_str.upper()
# print(result)

# Method 2:
reuslt = ""
for ch in my_str:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii - 32
        char = chr(new_ascii)
        reuslt += char
    else:
        reuslt += ch
print(reuslt)
