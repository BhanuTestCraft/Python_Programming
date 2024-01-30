# Dictionary and counter in Python to find winner of election.
input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john'] 
element_count = {}
for value in input:
    if value in element_count.keys():
        element_count[value]+=1
    else:
        element_count[value] =1
sorted_list = sorted(element_count.keys(),reverse=True)
sorted_vote = sorted(element_count.values(),reverse=True)
if sorted_vote[0]==sorted_vote[1]:
    print(f"The winer of election is : {sorted_list[1]}")
else:
    print(f"The winner of election is : {sorted_list[0]}")