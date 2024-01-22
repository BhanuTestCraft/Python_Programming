"""
Calculate sum of 5 subjects and Find percentage.
"""
total_marks = 500
marks_sub1 = float(input("Enter the marks obtained in subject1= "))
marks_sub2 = float(input("Enter the marks obtained in subject2= "))
marks_sub3 = float(input("Enter the marks obtained in subject3= "))
marks_sub4 = float(input("Enter the marks obtained in subject4= "))
marks_sub5 = float(input("Enter the marks obtained in subject5= "))
total_marks_obtained = marks_sub1 + marks_sub2 + marks_sub3 + marks_sub4 + marks_sub5
percentage_marks_obtained = (total_marks_obtained / total_marks) * 100
print(f"Percentage of marks obtained is {percentage_marks_obtained}")
