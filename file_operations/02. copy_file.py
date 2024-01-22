def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:  # loop will run until it get breaks intentionally.
        text = f1.read(100)
        print(text)
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()
    print("--------")
    f2 = open(newFile, "r")
    text1 = f2.read(100)
    print(text1)
    return


# Calling the function to execute the copy process of the file from old file to the new file.
copyFile(
    "/Users/bhanu/Personal/Python_Coding/file_operations/oldFile.txt",
    "/Users/bhanu/Personal/Python_Coding/file_operations/newFile.txt",
)
