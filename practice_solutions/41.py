"""
Write a program that calculates a person's BMI based on their height (in meters) and weight (in kilograms). Use the following formula: BMI = weight / (height^2). Then, classify the BMI according to the following ranges:
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater
"""
height = float(input("Enter the height of person in meter: "))
weight = float(input("Enter the wight of person in kg: "))
BMI = weight / (height**2)
print(f"BMI of person is {BMI:.2f}")
if BMI < 30:
    if BMI < 18.5:
        category = "Underweight"
    elif BMI >= 18.5 and BMI < -24.9:
        category = "Normal weight"
    elif BMI >= 25 and BMI <= 29.9:
        category = "Overweight"
else:
    category = "Obesity"
print("BMI Category:", category)
