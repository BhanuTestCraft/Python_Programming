# Store “name” of a student as Key, “list of 5 marks” of that student as a Value. Store atleast 5 student names. Print the sum and percentage of all the students.
student_dict={}
total_marks=500
for i in range(5):
    student_name=input(f"Enter the name of student {i+1} : ")
    student_marks=eval(input(f"Enter the marks obtained by {student_name}: "))
    student_dict[student_name]=student_marks

sum=0
for k,v in student_dict.items():
    for v in v:
        sum+=v
    percentage=(sum/total_marks)*100
    print(f"{k} - sum: {sum}, percentage: {percentage}")
    sum=0
