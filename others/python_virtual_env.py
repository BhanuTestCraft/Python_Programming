"""
Why python virtual env?
There exist two type of libraries in the python that are:
1. standard library: when we install the python then we get these libraries(Built-in modules and packages).
It is very difficult to host all the libraries in the standard distribution library so the dev has created the website name pypi on which all the rest of poackages and modules are hosted to use.
2. Third party package/modules: The packages hosted on pypi for the use when needed are known as third party packages/modules.
Eg: numpy 
---- These third party tool are installed using the pip(Preferred Installer Programor) or we can say it as python package manager.

-------------------
Let us assume we are having one operation system on which multiple application are hosted-----
mac os---> Two applications hosted i.e app1 and app2
assume app1: requires numpy version 1.19
assume app2: only work with numpy version 1.23
since we are having both the applications on the same os so we can only keep one of the numpy versions which will cause the issue in either of the application and that is the problem for us.

-------
To resolve this problem We need to create the virtual enviornment.
-------
python virtual env:
A self contained directory tree that contain python installation for a particular version of the python, plus a number of additional pacakges.
Visualization:------
MAC OS-----
1. Virtual Env(Base):--Package A(2.1), Package B(1.0)
2. Virtual Env(1):--   Package A(3.1), Package B(1.1)
3. Virtual Env(2):--   Package A(4.1), Package B(1.2)
Now we can work on all the applications on the dedicated env's without affecting the other applications.
"""