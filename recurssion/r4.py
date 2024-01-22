# print your name 10 times without using loop or manually.
count=0
def display_name():
    global count
    count+=1
    print("Bhanu")
    if count==10:
        return
    display_name()

display_name()