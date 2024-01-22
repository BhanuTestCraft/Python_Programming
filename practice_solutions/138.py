"""
Ask a string from user. Print the count of how many alphabets, digits, spaces and symbols (everything else) are there in that string.
"""
my_str = "abc12 3ABCD@ %$& #^&"
alpha_count = 0
digit_count = 0
space_count = 0
symbol_count = 0

for ch in my_str:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii < 122):
        alpha_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == " ":
        space_count += 1
    else:
        symbol_count += 1
print(f"Number of alphabet in the string are {alpha_count}")
print(f"Number of digit in the string are {digit_count}")
print(f"Number of spaces in the string are {space_count}")
print(f"Number of symbols in the string are {symbol_count}")
