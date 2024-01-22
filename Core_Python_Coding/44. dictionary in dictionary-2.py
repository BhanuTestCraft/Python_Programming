students_data={
    "Bhanu":{
        "roll_number":10,
        "gender": "male",
        "marks": [88,98,99,85,92]
    },
    "Sheetal":{
        "roll_number":11,
        "gender": "female",
        "marks": [81,56,76,87,90]
    },
    "Tushar":{
        "roll_number":23,
        "gender": "male",
        "marks": [90,45,67,87,81]
    }
}
for name,details in students_data.items():
    # print(f'{name} -> {sum(details["marks"])}')
    total=0
    for marks in details["marks"]:
        total+=marks
    print(f"{name} -> {total}")
