# f =open(oldFile.txt,"r")
# When we open any file in the read mode it will look for that file first in directory and if it will not find that file it will through an error.

# f =open(i=oldFile.txt,"w")
# When we do open any file in write mode then it will firstly look for that file and if there is no existence of such file, it will create one with the name provided.

# f = open("test_data.txt", "w")
# f.write("line one\nline two\nline three\n")
# f.close()


# The readline method reads all the characters up to and including the next newline
# character:
# f = open("test_data.txt", "r")
# print(f.readline())
# print(f.readlines())

# At the end of the file, readline returns the empty string and readlines returns
# the empty list:
# print(f.readline())  output: ""
# print(f.readlines()) output: []


def filterFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.readline()
        print(text)
        if text == "":
            break
        if text[0] == "#":
            continue
        f2.write(text)
    f1.close()
    f2.close()
    return


filterFile(
    "/Users/bhanu/Personal/Python_Coding/file_operations/oldFile.txt",
    "/Users/bhanu/Personal/Python_Coding/file_operations/newFile.txt",
)
