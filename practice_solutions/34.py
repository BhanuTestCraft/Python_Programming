"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not.
"""
classes_held = int(input("Enter the number of classes held= "))
claases_attended = int(input("Enter the classes attended= "))
per_attended = (claases_attended / classes_held) * 100
print(f"Percentage of classes attended are {per_attended:.1f}%")
if per_attended >= 75 and per_attended <= 100:
    print("Student is allowed to sit in examination")
elif per_attended < 75:
    print("Student is not allowed to sit in examination")
else:
    print("Inavid")
