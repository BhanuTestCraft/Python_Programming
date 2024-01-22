# Write a program that displays the name of the student that has scored highest marks overall.
student_marks={
    "John":{"Marks":[80,85,90]},
    "Alice":{"Marks":[75,88,92]},
    "Bob":{"Marks":[90,92,88]}
}
highest_marks=0
highest_scoring_student=None
for student,element in student_marks.items():
    total=0
    for list in element.values():
        for marks in list:
            total+=marks
    if total>highest_marks:
        highest_marks=total
        highest_scoring_student=student
    
print(f"{highest_scoring_student} scored the highest marks of {highest_marks}")