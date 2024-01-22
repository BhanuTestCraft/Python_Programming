# Convert two lists into a dictionary. Make two list on your own of same length, and convert them to dictionary.

list1=["Ten","Twenty","Thirty"]
list2=[10,20,30]
my_dict={}
# len(list1)==len(list2)
for i in range(len(list1)):
    my_dict[list1[i]]=list2[i]

print(my_dict)