# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Calling functions:
# You can call these functions like any other Python callable. This example uses the time() function, which returns system time in seconds since the Unix
# epoch, and the GetModuleHandleA() function, which returns a win32 module handle.
#

# 
# This example calls both functions with a NULL pointer (None should be used as the NULL pointer):
# 

print(libc.time(None))  

# OUTPUT: '1150640792'

print(hex(windll.kernel32.GetModuleHandleA(None)))  

# OUTPUT: '0x1d000000'

 
#
# Note:
# ctypes may raise a ValueError after calling the function, if it detects that an invalid number of arguments were passed.
# This behavior should not be relied upon. It is deprecated in 3.6.2, and will be removed in 3.7.
#

# 
# ValueError is raised when you call an stdcall function with the cdecl calling convention, or vice versa:
# 

cdll.kernel32.GetModuleHandleA(None)  


windll.msvcrt.printf(b"spam")  

#
# To find out the correct calling convention you have to look into the C header file or the documentation for the function you want to call.
#

# 
# On Windows, ctypes uses win32 structured exception handling to prevent crashes from general protection faults when functions are called with invalid
# argument values:
# 

windll.kernel32.GetModuleHandleA(32)  
