# else block with try-except-finally
"""
1. if-else: if the condtion in if block is false then only the esle block will get executed.
2. for-else: if loop executed without break then only else will be executed.
3. while-else: if loop executed without break then only else will be executed.
4. else block will only get executed when there is no exception raised in the try block when we are using else with try-except-finally.
5. When we are writing the else block it is compulsary to write the except block else it will give the syntax error.
"""

# order : try-->except-->else-->finally
"""
try:
    risky code
except:
      Handling code
      it will be executed only if there is exception in try block.
else:
    it will be excuted if there is no exception in try block.
finally:
       cleanup code
       executed always.
"""

try:
    print("try")
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
# output:
# try
# else
# finally
    
try:
    print("try")
    print(10/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
# output:
# try
# except
# finally
    
f=None
try:
    f=open("abc.txt","r")
except:
    print("Problem while opening and locating the file.")
else:
    print("file opened successfully")
    print(f.read())
finally:
    if f is not None:
        f.close()
