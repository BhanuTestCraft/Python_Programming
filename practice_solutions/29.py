"""
Write a program to print the last digit of a number.
Example 1
Input: 45321
Output: 1

Example 2
Input: 459094
Output: 4
concept-- When we divide any number by 10 then in that case the remender will always be the unit digit of that number.
"""
num = int(input("Enter the number= "))
last_digit = num % 10
print(f"The last digit of the number {num} is {last_digit}")
