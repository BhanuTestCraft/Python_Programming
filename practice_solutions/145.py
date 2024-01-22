# Write a Python program to sum all the items in a dictionary.
my_dict={"physics":98,
         "maths":90,
         "english":91,
         "Hindi":88,
         "history":58,
         }

# Method 1:
total=0
for v in my_dict.values():
    total+=v
print(f"Total marks is {total}")