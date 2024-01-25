# control flow in try except and finally block
"""
try:
   statement 1
   statement 2
   statement 3
except:
      staement 4
finally: 
      statement 5
statement 6
"""

# case 1: When there is no exception
# --> statement 1,2,3,5 and 6 will be getting executed. This is the normal termination.

# case 2: if the exception occur at statement 2 and corresponding except block matched.
# --> statements 1,4,5,6 will be getting executed. This is the normal termination.

# case 3: if the exception occur at statement 2 and corresponding except block not matched.
# --> statements 1,5 will be getting executed and this is abnormal termination.

# case 4: if the exception is raised at the statement 4
# --> it is an abnormal termination before running the finally block.

# case 5: if the exception raised at statement 5 or 6.
# --> It is always abnormal termination.