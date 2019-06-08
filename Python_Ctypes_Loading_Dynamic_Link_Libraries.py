# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Loading dynamic link libraries.
# ctypes exports the cdll, and on Windows windll and oledll objects, for loading dynamic link libraries.
# You load libraries by accessing them as attributes of these objects.
# cdll loads libraries which export functions using the standard cdecl calling convention, while windll libraries call functions using the stdcall calling
# convention. 
# oledll also uses the stdcall calling convention, and assumes the functions return a Windows HRESULT error code.
# The error code is used to automatically raise an OSError exception when the function call fails.
#

#
# Here are some examples for Windows.
# Note that msvcrt is the MS standard C library containing most standard C functions, and uses the cdecl calling convention:
# 

from ctypes import *

print(windll.kernel32)  

# OUTPUT: '<WinDLL 'kernel32', handle ... at ...>'

print(cdll.msvcrt)      

# OUTPUT: '<CDLL 'msvcrt', handle ... at ...>'

libc = cdll.msvcrt      

#
# Windows appends the usual .dll file suffix automatically.
# 

#
# Note:
# Accessing the standard C library through cdll.msvcrt will use an outdated version of the library that may be incompatible with the one being used by
# Python.
# Where possible, use native Python functionality, or else import and use the msvcrt module.
# On Linux, it is required to specify the filename including the extension to load a library, so attribute access can not be used to load libraries.
# Either the LoadLibrary() method of the dll loaders should be used, or you should load the library by creating an instance of CDLL by calling the
# constructor:
# 

cdll.LoadLibrary("libc.so.6")  

# OUTPUT: '<CDLL 'libc.so.6', handle ... at ...>'

libc = CDLL("libc.so.6")       
libc                           

# OUTPUT: '<CDLL 'libc.so.6', handle ... at ...>'
