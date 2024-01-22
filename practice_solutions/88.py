"""
Print the following pattern.
        *
      * * *
    * * * * * 
  * * * * * * *
* * * * * * * * *
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     for m in range(1,i):
#         print("*",end=" ")
#     print()

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range((i * 2) - 1):
        print("*", end=" ")
    print()
