# Store marks of 5 different subjects in a dictionary. Ask subject name as an input from the User. Print the marks of that subject entered by User. If subject does not exist, print “Invalid”.
subject_marks_dict={"physics":90,
         "maths":92,
         "english":93,
         "Hindi":94,
         "history":95,
         }

subject_name=input("Enter the name of subject = ")
if subject_name in subject_marks_dict.keys():
    print(f"marks in {subject_name} is {subject_marks_dict[subject_name]}")
else:
    print(f"Entered subject {subject_name} is an Invalid input !!")