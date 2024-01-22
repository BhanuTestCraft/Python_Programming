# variables: python variables are container for storing the data values.unlike other languages, such as java, Python has no command for declaring the variable, so you create one the moment you first assign the value to it.

"""
Rules to name a variable:
1. variables must start with a letter or an underscore.
2. variable names can only contain letter,numbers,and underscores.special character and spaces are not allowed.
3. variable name are case sensitive(myvar and myVar are treated as different variables.)
4. variable names should be descriptive and indicate the purpose of the variable(eg: count,name,toatl_amount etc..)
5. It's recommended to use the lowercase letters for the variable names, and for names with multiple words,use undercore to separate them(snake_case)
"""

x=5
y=25
print("x") #Normally whatever we put in the double quote print statement will print the same inside the quote.
print(x) #It will print the value of x.
print(y)
name="Bhanu"
age=25
gender="male"
print(f"Name:{name},Age:{age},Gender:{gender}") #using F-string
print(name)
print("Name:",name)
print(age)
print("Age:",age)
print(gender)
print("Gender:",gender)
print(name,end=" ")
print(age,end=" ")
print(gender)

first_name="Bhanu"
last_name="Pratap"
print(first_name)
print(last_name)
print(first_name,end=" ")
print(last_name)
print(f"first_name:{first_name},last_name:{last_name}")