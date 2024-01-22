# Create another nested dictionary named additional_marks with information for two more students. Merge this dictionary with the student_marks dictionary.
student_marks={
    "John":{"Marks":[80,85,90]},
    "Alice":{"Marks":[75,88,92]},
    "Bob":{"Marks":[90,92,88]}
}
additional_marks={
    "Bhanu":{"Marks":[76,89,99]},
    "Tushar":{"Marks":[50,72,98]}
}
for k,v in additional_marks.items():
    student_marks[k]=v
print(student_marks)