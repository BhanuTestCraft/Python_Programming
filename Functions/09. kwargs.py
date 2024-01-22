def add(**kwargs):
    print(kwargs)
    # kwargs is a dictionary and used when we don't know how many named arguments are required.
    for k, v in kwargs.items():
        print(k, v)


add(name="Bhanu", age=27, gender="male")
