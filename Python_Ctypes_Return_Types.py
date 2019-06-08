# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Return types
# By default functions are assumed to return the C int type. Other return types can be specified by setting the restype attribute of the function object.
#

# 
# Here is a more advanced example, it uses the strchr function, which expects a string pointer and a char, and returns a pointer to a string:
# 

strchr = libc.strchr
strchr(b"abcdef", ord("d"))  

# OUTPUT: '8059983'

strchr.restype = c_char_p    # c_char_p is a pointer to a string
strchr(b"abcdef", ord("d"))

# OUTPUT: 'b'def''

print(strchr(b"abcdef", ord("x")))

# OUTPUT: 'None'

# 
# If you want to avoid the ord("x") calls above, you can set the argtypes attribute, and the second argument will be converted from a single character
# Python bytes object into a C char:
# 

strchr.restype = c_char_p

strchr.argtypes = [c_char_p, c_char]
strchr(b"abcdef", b"d")

# OUTPUT: 'def'

strchr(b"abcdef", b"def")

print(strchr(b"abcdef", b"x"))

# OUTPUT: 'None'

strchr(b"abcdef", b"d")

# OUTPUT: 'def'

# 
# You can also use a callable Python object (a function or a class for example) as the restype attribute, if the foreign function returns an integer.
# The callable will be called with the integer the C function returns, and the result of this call will be used as the result of your function call.
# This is useful to check for error return values and automatically raise an exception:
# 

GetModuleHandle = windll.kernel32.GetModuleHandleA  

def ValidHandle(value):
        if value == 0:
            raise WinError()

        return value

GetModuleHandle.restype = ValidHandle  
GetModuleHandle(None)  

# OUTPUT: '486539264'

GetModuleHandle("something silly")  
