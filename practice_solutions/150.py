# Store name as a Key, and 5 marks in a List as a value in dictionary. Store details of at least 5 students. Print the name of the student who got highest marks.

student_data={
    "student1":[90,92,94,88,45],
    "student2":[78,90,99,56,74],
    "student3":[35,90,99,98,78],
    "student4":[78,89,67,90,99],
    "student5":[87,88,89,56,98],
}
highest_marks=0
student_name=""
for k,v in student_data.items():
    sum=0
    for v in v:
        sum+=v
    if sum>highest_marks:
        highest_marks=sum
        student_name=k
print(f"{student_name} got the highest marks = {highest_marks}")
    