# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Callback functions:
# ctypes allows creating C callable function pointers from Python callables.
# These are sometimes called callback functions.
#

# 
# First, you must create a class for the callback function.
# The class knows the calling convention, the return type, and the number and types of arguments this function will receive.
# The CFUNCTYPE() factory function creates types for callback functions using the cdecl calling convention. On Windows, the WINFUNCTYPE() factory function
# creates types for callback functions using the stdcall calling convention.
#

# 
# Both of these factory functions are called with the result type as first argument, and the callback functions expected argument types as the remaining
# arguments.
#

# 
# I will present an example here which uses the standard C library’s qsort() function, that is used to sort items with the help of a callback function.
# qsort() will be used to sort an array of integers:
# 

IntArray5 = c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)

qsort = libc.qsort

qsort.restype = None

# 
# qsort() must be called with a pointer to the data to sort, the number of items in the data array, the size of one item, and a pointer to the comparison
# function, the callback.
# The callback will then be called with two pointers to items, and it must return a negative integer if the first item is smaller than the second, a zero
# if they are equal, and a positive integer otherwise.
#

# 
# So our callback function receives pointers to integers, and must return an integer. First we create the type for the callback function:
# 

CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

# 
# To get started, here is a simple callback that shows the values it gets passed:
# 

def py_cmp_func(a, b):
        print("py_cmp_func", a[0], b[0])

        return 0

cmp_func = CMPFUNC(py_cmp_func)

# 
# The result:
# 

qsort(ia, len(ia), sizeof(c_int), cmp_func)  

#
# Now we can actually compare the two items and return a useful result:
# 

def py_cmp_func(a, b):
        print("py_cmp_func", a[0], b[0])

        return a[0] - b[0]

qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func)) 

# 
# As we can easily check, our array is sorted now:
# 

for i in ia: print(i, end=" ")

# OUTPUT: '1 5 7 33 99
 
#
# The function factories can be used as decorator factories, so we may as well write:
# 

@CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

def py_cmp_func(a, b):
        print("py_cmp_func", a[0], b[0])

        return a[0] - b[0]

qsort(ia, len(ia), sizeof(c_int), py_cmp_func)

#
# Note:
# Make sure you keep references to CFUNCTYPE() objects as long as they are used from C code.
# ctypes doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.
# Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback),
# ctypes creates a new dummy Python thread on every invocation.
# This behavior is correct for most purposes, but it means that values stored with threading.local will not survive across different callbacks, even when
# those calls are made from the same C thread.
#