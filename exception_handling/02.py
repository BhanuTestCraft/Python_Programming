"""
1. Every exception got raised during the run time is itself a class.
2. Whenever there is exception raised pvm will create one object for that erro class.
3. Immediately pvm will check any handling code is there or not. and if we have written the code to handle that exception then it will jump to that part of the code and will execute the rest of the program normally.
4. If we have not written the handling code for that exception then the program will terminate itself immediately on that line of the code and print the exception in the comnsole without executing the rest of the program and this is the abnormal termination.

Python Exception heirarchy:
Since python bydefault handles the error by raising the certain exceptions mentioned below and that is termed as default exception handling
BaseException is the parent class of all the exception.
1. Exception : child class of the BaseException.
2. SystemExit : child class of the BaseException.
3. GeneratorExit : child class of the BaseException.
4. KeyboardInterrupt : child class of the BaseException.

Exception:
Arithemetic error:: child class of the Exception.
1. ZeroDivisonError : child class of the Arithemetic error.
2. OverflowError : child class of the Arithemetic error.
3. FloatingPointError : child class of the Arithemetic error.
LookUpError:: child class of the Exception.
1. IndexError
2. KeyError
OSError:: child class of the Exception.
1. FileNotFoundError
2. InterruptedError
3. TimeOutError
4. PermissionError
NameError
TypeError
ValueError
EofError

In conclusin we can say that while programming we do focus on the exception base class of BaseException and it's child classes like arithemeticerror,lookuperror,oserror,nameerror,typeerror,valuerror,eoferror.
"""
