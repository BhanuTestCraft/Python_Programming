# Ask subject name and marks from the user and keep adding it to dictionary.
marks={}
subject_count=int(input("Enter the no of subjects = "))
for _ in range(0,subject_count):
    # When we do not have any use of the index we can use underscore to help us in iteration. 
    subject_name=input("Enter the subject name = ")
    subject_marks=int(input(f"Enter marks for {subject_name} = "))
    marks[subject_name]=subject_marks

print(marks)