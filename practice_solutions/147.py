# Ask a string from user. Display the dictionary where each key is a character and value is the frequency of that character that comes in that string.
my_string=input("Enter any string value = ")
my_dict={}
for ch in my_string:
    if ch not in my_dict.keys():
        my_dict[ch]=1
    else:
        my_dict[ch]+=1
print(my_dict)
