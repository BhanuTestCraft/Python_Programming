student_data={
    "Bhanu":{
        "roll_number":10,
        "gender": "male",
        "physics": 98,
        "Chemistry": 96,
        "Maths": 89,
    },
    "Sheetal":{
        "roll_number":11,
        "gender": "female",
        "physics": 88,
        "Chemistry": 76,
        "Maths": 71,
    },
    "Tushar":{
        "roll_number":23,
        "gender": "male",
        "physics": 99,
        "Chemistry": 56,
        "Maths": 90,
    }
}

print(student_data["Bhanu"])
print(student_data["Bhanu"]["roll_number"])
print(student_data["Bhanu"]["gender"])

"""
"Bhanu" -> x marks
"Sheetal" -> y marks
"Tushar" -> z marks
"""
for name,details in student_data.items():
    print(f'{name} -> {details["physics"]+details["Chemistry"]+details["Maths"]}') 

#output:
# Bhanu -> 283
# Sheetal -> 235
# Tushar -> 245