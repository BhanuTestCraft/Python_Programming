"""
Count the number of spaces in a string entered by user.
"""
my_str = "ab c 123 AB CD"
space_count = 0
for ch in my_str:
    if ch == " ":
        space_count += 1
print(f"Number of spaces in string is {space_count}")
