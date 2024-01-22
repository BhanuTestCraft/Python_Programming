"""
Ask a string from user. Count how many alphabets are there in that string.
"""
my_str = "abc123"

# Iterate by index.
# count = 0
# for i in range(0, len(my_str)):
#     if my_str[i].isalpha():
#         count += 1

# print(f"No of alphabets in the given string are {count}")

# Iterate by value.
# count = 0
# for ch in my_str:
#     if ch.isalpha():
#         count += 1
# print(f"No of alphabets in the given string are {count}")

count = 0
for ch in my_str:
    ascii = ord(ch)
    if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
        count += 1

print(f"No of alphabets in the given string are {count}")
