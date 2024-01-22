# Question: Explain the use of escape sequences in Python and provide examples of how they can be used in strings.

# Answer:

# Escape sequences in Python are used to include special characters within strings. They begin with a backslash (\) followed by a character or combination of characters. Here are some common escape sequences:
# \n: Newline
# \t: Tab
# \': Single quote
# \": Double quote
# \\: Backslash
# Here we are learning about the escape sequences in python.
print("Hello world")
print("This is code and debug")

# Here we are using new line escape sequence.
# We will not be able to see the escape character in output but they will do there work.
print("Hello \nWorld")
print("Hello world\nThis is code and debug")
print("my name is bhanu\nmy age is 27\nmy gender is male")

# Here we are using tab escape character.
print("Hello \t\tWorld")
print("This is\t\tcode and debug")

# Here we are using double quote.
# output= This is "Code and Debug"
print('She said, "Hello!".')
print("She said, \"Hello!\".")
print('This is "Code and Debug"')
print("This is \"Code and Debug\"")

# Here we are using single quote
# output= This is 'Code nand Debug'
print("She said, 'Hello!'.")
print("She said, \'Hello!\'.")
print('This is \'Code and Debug\'')

# Here we are using \\
# output=  my name is B\hanu Pratap
print("This is a bacslash: \\")
print("my name is B\hanu Pratap")
print("my name is A\nirudh Pareek") #Here it will not print the same and will lead output in the next line so if we need to add backsalsh intentionally then we need to put \\
print("my name is A\\nirudh pareek")

# Questions 1-3
# output1=C:\Users\John\Desktop\File.txt
print("C:\\Users\\John\\Desktop\\File.txt")

# output2=He said, "Hello!".
print("He said, \"Hello!\".")

# output3=She said, 'It's cold'.
print("she said, \'It's cold\'.")