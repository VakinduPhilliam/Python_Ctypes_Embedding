# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Specifying the required argument types (function prototypes):
# It is possible to specify the required argument types of functions exported from DLLs by setting the argtypes attribute.
# argtypes must be a sequence of C data types (the printf function is probably not a good example here, because it takes a variable number and different
# types of parameters depending on the format string, on the other hand this is quite handy to experiment with this feature):
# 

printf.argtypes = [c_char_p, c_char_p, c_int, c_double]
printf(b"String '%s', Int %d, Double %f\n", b"Hi", 10, 2.2)

#
# OUTPUT:
#
# String 'Hi', Int 10, Double 2.200000
# 37

# 
# Specifying a format protects against incompatible argument types (just as a prototype for a C function), and tries to convert the arguments to valid
# types:
# 

printf(b"%d %d %d", 1, 2, 3)

printf(b"%s %d %f\n", b"X", 2, 3)

#
# OUTPUT:
#
# X 2 3.000000
# 13
