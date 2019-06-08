# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.

#
# Calling functions
# Note that printf prints to the real standard output channel, not to sys.stdout, so these examples will only work at the console prompt, not from within
# IDLE or PythonWin:
# 

printf = libc.printf
printf(b"Hello, %s\n", b"World!")

#
# OUTPUT:
#
# Hello, World!
# 14

printf(b"Hello, %S\n", "World!")

#
# OUTPUT:
#
# Hello, World!
# 14

printf(b"%d bottles of beer\n", 42)

#
# OUTPUT:
#
# 42 bottles of beer
# 19

printf(b"%f bottles of beer\n", 42.5)

#
# All Python types except integers, strings, and bytes objects have to be wrapped in their corresponding ctypes type, so that they can be converted to the
# required C data type:
# 

printf(b"An int %d, a double %f\n", 1234, c_double(3.14))

#
# OUTPUT:
#
# An int 1234, a double 3.140000
# 31
#
