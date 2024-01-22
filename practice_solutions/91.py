"""
Print the following pattern
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * * 
  * * * * * * *
* * * * * * * * *
"""
for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range((i * 2) - 1):
        print("*", end=" ")
    print()
for i in range(1, 5):
    for j in range(i, 4):
        print(" ", end=" ")
    for k in range((2 * i) + 1):
        print("*", end=" ")
    print()
