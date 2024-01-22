"""
Write a program that converts a string in camelCase to snake_case. For example converting "helloWorldHowAreYou" should result in "hello_world_how_are_you".
"""
camel_string = "helloWorldHowAreYou"
words_list = [camel_string[0]]

for char in camel_string[1:]:
    if char.isupper():
        words_list.append(char.lower())
    else:
        words_list[-1] += char

snake_string = "_".join(words_list)
print(snake_string)
