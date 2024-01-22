# Given a list and dictionary, map each element of list with each item of dictionary, forming nested dictionary as value.
test_dict={"anirudh":45,"coder":75,"raj":99}
test_list=[11,14,7]
result={}
for i in test_list:
    for k,v in test_dict.items():
        result[i]={k:v}
        test_dict.pop(k)
        break
print(result)
