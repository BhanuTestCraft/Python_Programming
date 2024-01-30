# Python | Ways to remove a key from dictionary.

input_dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
del input_dict["Anuradha"]
print(f"dict after removing key is {input_dict}")

input_dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
input_dict.pop("Mani")
print(input_dict)

input_dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
new_dict ={key:val for key,val in input_dict.items() if key!="Arushi"}
print(new_dict)

input_dict = {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
dict = {}
for key,value in input_dict.items():
    if key!= "Arushi":
        dict[key]=value
print(dict)