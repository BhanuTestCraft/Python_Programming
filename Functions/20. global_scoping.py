a = 15


def change():
    global a
    a = 30
    print(a)


print(a)
change()
print(a)
# output
# 15
# 30
# 30
