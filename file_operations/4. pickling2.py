import pickle

# Writing to the file in binary mode ("wb") because pickle deals with binary data.
f = open("/Users/bhanu/Personal/Python_Coding/file_operations/pic.txt", "wb")

# To store a data structure, use the dump method and then close the file in the usual
# way.
pickle.dump(12.3, f)
pickle.dump([1, 2, 3], f)
f.close()

# Reading from the file in binary mode ("rb") because pickle deals with binary data.
# Then we can open the file for reading and load the data structures we dumped:
f = open("/Users/bhanu/Personal/Python_Coding/file_operations/pic.txt", "rb")
x = pickle.load(f)
y = pickle.load(f)

print(x, type(x))
print(y, type(y))
