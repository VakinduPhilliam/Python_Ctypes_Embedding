# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Calling functions with your own custom data types:
# You can also customize ctypes argument conversion to allow instances of your own classes be used as function arguments.
# ctypes looks for an _as_parameter_ attribute and uses this as the function argument.
# Of course, it must be one of integer, string, or bytes:
# 

class Bottles:
        def __init__(self, number):
            self._as_parameter_ = number

bottles = Bottles(42)

printf(b"%d bottles of beer\n", bottles)

#
# OUTPUT: 
#
# 42 bottles of beer
# 19
#