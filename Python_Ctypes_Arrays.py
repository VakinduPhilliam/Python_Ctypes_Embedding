# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Arrays:
# Arrays are sequences, containing a fixed number of instances of the same type.
#

# 
# The recommended way to create array types is by multiplying a data type with a positive integer:
# 

TenPointsArrayType = POINT * 10

# 
# Here is an example of a somewhat artificial data type, a structure containing 4 POINTs among other stuff:
# 

from ctypes import *

class POINT(Structure):
        _fields_ = ("x", c_int), ("y", c_int)

class MyStruct(Structure):
        _fields_ = [("a", c_int),
                    ("b", c_float),
                    ("point_array", POINT * 4)]

print(len(MyStruct().point_array))

# OUTPUT: '4'

# 
# Instances are created in the usual way, by calling the class:
# 

arr = TenPointsArrayType()

for pt in arr:

        print(pt.x, pt.y)

# 
# The above code print a series of 0 0 lines, because the array contents is initialized to zeros.
#

# 
# Initializers of the correct type can also be specified:
# 

from ctypes import *

TenIntegers = c_int * 10

ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(ii)

# OUTPUT: '<c_long_Array_10 object at 0x...>'

for i in ii: print(i, end=" ")

#   ...

# OUTPUT: '1 2 3 4 5 6 7 8 9 10'
