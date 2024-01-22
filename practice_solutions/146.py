# Write a Python program to multiply all the items in a dictionary.
my_dict={"physics":1,
         "maths":2,
         "english":3,
         "Hindi":4,
         "history":5,
         }
total=1
for v in my_dict.values():
    total*=v
print(total)