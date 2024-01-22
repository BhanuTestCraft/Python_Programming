"""
Ask a string from user. Convert all the alphabets to lowercase.
"""
my_str = "abc123ABCD"

# Method 1:
# result = my_str.lower()
# print(result)

# Method 2:
result = ""
for ch in my_str:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        new_ascii = ascii + 32
        char = chr(new_ascii)
        result += char
    else:
        result += ch
print(result)
