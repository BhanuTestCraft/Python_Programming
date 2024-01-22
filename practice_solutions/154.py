# Write a python program that prints all the students name along with their average marks.
student_marks={
    "John":{"Marks":[80,85,90]},
    "Alice":{"Marks":[75,88,92]},
    "Bob":{"Marks":[90,92,88]}
}
for student,element in student_marks.items():
    total=0
    for list in element.values():
        for marks in list:
           total+=marks
    average_marks=(total/3)
    print(f"{student}: {average_marks}")