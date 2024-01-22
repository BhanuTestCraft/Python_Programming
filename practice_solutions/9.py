"""
Write a program that converts a temperature in Fahrenheit to Celsius. The formula is:
Celsius = (Fahrenheit - 32) * 5/9
"""
temp_in_fahrenheit = float(input("Enter the temperature value in Fahrenheit= "))
temp_in_celsius = (temp_in_fahrenheit - 32) * 5 / 9
print(f"The value of temperature in celsius is {temp_in_celsius} ")
print(f"{temp_in_fahrenheit} fahrenheit = {temp_in_celsius} celsius")
