# Write a Python program to combine two dictionary by adding values for common keys.
d1={"a":100,"b":200,"c":300,"d":400}
d2={"a":200,"b":300,"c":400,"d":500}
new_dict={}
for k,v in d1.items():
        new_dict[k]=v
for k,v in d2.items():
    if k not in new_dict.keys():
        new_dict[k]=v 
    else: 
        new_dict[k]+=v 
print(new_dict)