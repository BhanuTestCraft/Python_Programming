"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
1.Print percentage of class attended
2.Print Is student is allowed to sit in exam or not.
"""
total_classes = int(input("Enter the total classes held= "))
attended_classes = int(input("Enter the attended classes= "))
per_class_attended = (attended_classes / total_classes) * 100
print(f"percentage classes attended is {per_class_attended:.3f}%")
if per_class_attended >= 75:
    print("Student allowed to sit in exam")
else:
    print("student is not allowed to sit in exam")
