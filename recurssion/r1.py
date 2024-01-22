# recurssion: when a function calls itself, then that function is called recursive function and process is called as recurssion.
import sys

print(sys.getrecursionlimit())
# By default recurssion limit is 1000 and after that we will get some error like: RecursionError: maximum recursion depth exceeded while calling a Python object.
# If we need to set the recurssion limit we can use:
sys.setrecursionlimit(200)
count=0
def demo():
    global count
    count+=1
    print("Hey Hi Bye!!",count)
    demo()

demo()