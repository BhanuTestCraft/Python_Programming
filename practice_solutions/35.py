"""
Take the salary as input from user and update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""
current_sal = int(input("Enter the current salary= "))
if current_sal >= 50000:
    increment = 20
elif current_sal >= 20000 and current_sal < 50000:
    increment = 15
elif current_sal >= 10000 and current_sal < 20000:
    increment = 10
else:
    increment = 5
print(f"Congratulations you got an increment of {increment}% this year.")
updated_sal = current_sal + ((increment * current_sal / 100))
print(f"your updated salary will be {updated_sal} this year.")
