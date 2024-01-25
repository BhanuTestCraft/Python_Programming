# Control flow in the try except block.

"""
try: 
   statement 1
   statement 2
   statement 3
except:
   statement 4
statement 5

case 1: If there will be no exception will running the program
--> Except block will not be getting executed.
--> so only statement 1,2,3,4 will only get executed.

case 2: An exception raised while running statement 2 and corresponding except block matched.
-->  statement 1,4,5 will be getting executed and normal termination will happen.
--> since on exception occur program will shift to the except block and it will never come back in try block so mostly we write as minimum code in the try block.

case 3: An exception raised at the statement 2 but corresponding except block is not matched
--> only statement 1 will run and there is abnormal termination.

case 4: An exception raised at the statement 4 or at statement 5
--> It will always lead to the abnormal termination.
"""