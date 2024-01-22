"""
To handle multiple conditions.
To understand this we will ask two input from the user and print which number is greatest.
syntax-->
if condition1:
    line to be executed if condition is true.
elif condition2:
    line to be executed if condition is true.
elif condition3:
    line to be executed if condition is true.
else:
    line to be executed at last if none of condition is true.

else condtion is not mandatory statement.
"""
# num1=int(input("Enter number 1 = "))
# num2=int(input("Enter number 2 = "))
# if num1>num2:
#     print("num1 is greater number")
# elif num2>num1:
#     print("num2 is greater number")
# else:
#     print("Both numbers are equal")

"""
Ask 5 marks from the user.
calculate percentage and print it.

91-100-->A grade
81-90--> B grade
71-80--> C grade
61-70--> D grade
1-60---> Fail
Rest print invalid.
"""
total_marks=500
m1=float(input("Enter the marks in subject 1= "))
m2=float(input("Enter the marks in subject 2= "))
m3=float(input("Enter the marks in subject 3= "))
m4=float(input("Enter the marks in subject 4= "))
m5=float(input("Enter the marks in subject 5= "))
per_marks=((m1+m2+m3+m4+m5)/total_marks)*100
print(f"percentage marks obtained is {per_marks}")
if 91<=per_marks<=100:
    print("You got grade A")
elif 81<=per_marks<=90:
    print("You got grade B")
elif 71<=per_marks<=80:
    print("You got grade C")
elif 61<=per_marks<=70:
    print("You got grade D")
elif 1<=per_marks<=60:
    print("FAIL")
else:
    print("Invalid Percentage")