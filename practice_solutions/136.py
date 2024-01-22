"""
Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and don’t change the other letters.
"""
my_str = "abc123ABCD"
result = ""
for ch in my_str:
    ascii = ord(ch)
    if ascii >= 65 and ascii <= 90:
        lower_ascii = ascii + 32
        char = chr(lower_ascii)
        result += char
    elif ascii >= 97 and ascii <= 122:
        upper_ascii = ascii - 32
        char = chr(upper_ascii)
        result += char
    else:
        result += ch
print(result)
