"""
Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)
"""
# method1
# my_list=["a","e","i","o","u"]
# chr=input("Enter any character= ")
# if chr in my_list:
#     print("Entered character is vowel")
# else:
#     print("Entered charcter is consonat")

# method2
char = input("Enter any character= ")
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("Entered charcter is vowel")
else:
    print("Entered charcter is consonant")
