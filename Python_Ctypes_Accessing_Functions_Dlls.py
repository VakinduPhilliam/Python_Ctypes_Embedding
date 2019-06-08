# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Accessing functions from loaded dlls:
# 
# Functions are accessed as attributes of dll objects.
# 

from ctypes import *

libc.printf

# OUTPUT: '<_FuncPtr object at 0x...>'

print(windll.kernel32.GetModuleHandleA)  

# OUTPUT: '<_FuncPtr object at 0x...>'

print(windll.kernel32.MyOwnFunction)   

#
# windll does not try to select one of them by magic, you must access the version you need by specifying GetModuleHandleA or GetModuleHandleW explicitly,
# and then call it with bytes or string objects respectively.
#

# 
# Sometimes, dlls export functions with names which aren’t valid Python identifiers, like "??2@YAPAXI@Z".
# In this case you have to use getattr() to retrieve the function:
# 

getattr(cdll.msvcrt, "??2@YAPAXI@Z")  

# OUTPUT: '<_FuncPtr object at 0x...>'

# 
# On Windows, some dlls export functions not by name but by ordinal.
# These functions can be accessed by indexing the dll object with the ordinal number:
# 

cdll.kernel32[1]  

# OUTPUT: '<_FuncPtr object at 0x...>'

cdll.kernel32[0]  
