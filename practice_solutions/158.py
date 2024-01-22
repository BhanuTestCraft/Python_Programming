# Remove the entry for the student "John" from the student_marks dictionary.
student_marks={
    "John":{"Marks":[80,85,90]},
    "Alice":{"Marks":[75,88,92]},
    "Bob":{"Marks":[90,92,88]}
}
student_marks.pop("John")
print(student_marks)    