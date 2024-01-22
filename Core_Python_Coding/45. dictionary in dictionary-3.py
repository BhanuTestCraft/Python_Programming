students_data={
    "Bhanu":{
        "roll_number":10,
        "gender": "male",
        "marks": {"physics":98,"Chemistry":89,"Maths":99}
    },
    "Sheetal":{
        "roll_number":11,
        "gender": "female",
        "marks": {"physics":78,"Chemistry":81,"Maths":75}
    },
    "Tushar":{
        "roll_number":23,
        "gender": "male",
        "marks": {"physics":68,"Chemistry":80,"Maths":86}
    }
}
for name,details in students_data.items():
    total=0
    for v in details["marks"].values():
        total+=v
    print(f"{name} -> {total}")