def add(n1, n2, n3, *args, **kwargs):
    print(f"{n1=}")
    print(f"{n2=}")
    print(f"{n3=}")
    print(f"{args=}")
    print(f"{kwargs=}")


# add(10, 20, 30)
# add(10, 20, 30, 100, 200, 300)
add(10, 20, 30, 100, 200, 300, name="Bhanu", age=27, gender="male")
