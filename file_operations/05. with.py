# Without using with statement
file = open("example.txt", "r")
try:
    content = file.read()
    # Process the content
finally:
    file.close()

# Using with statement
with open("example.txt", "r") as file:
    content = file.read()
    # Process the content
# File is automatically closed when exiting the block

# In the second example, the with statement ensures that the file is closed automatically when the block is exited, making the code more concise and readable.
