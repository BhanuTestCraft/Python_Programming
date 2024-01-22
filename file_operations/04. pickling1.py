f = open("/Users/bhanu/Personal/Python_Coding/file_operations/pic.txt", "w")
f.write(str(12.3))
f.write(str([1, 2, 3]))
f.close()
f = open("/Users/bhanu/Personal/Python_Coding/file_operations/pic.txt", "r")
text = f.readline()
print(text, type(text))
# output: 12.3[1, 2, 3] <class 'str'>

# The problem is that when you read the value back, you get a string. The original
# type information has been lost. In fact, you can’t even tell where one value ends
# and the next begins.

# The solution is pickling, so called because it “preserves” data structures. The
# pickle module contains the necessary commands. To use it, import pickle and
# then open the file in the usual way.
