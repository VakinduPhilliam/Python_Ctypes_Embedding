# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Structures and unions:
# Structures and unions must derive from the Structure and Union base classes which are defined in the ctypes module.
# Each subclass must define a _fields_ attribute. _fields_ must be a list of 2-tuples, containing a field name and a field type.
#

# 
# The field type must be a ctypes type like c_int, or any other derived ctypes type: structure, union, array, pointer.
#

# 
# Here is a simple example of a POINT structure, which contains two integers named x and y, and also shows how to initialize a structure in the constructor:
# 

from ctypes import *

class POINT(Structure):
        _fields_ = [("x", c_int),
                    ("y", c_int)]

point = POINT(10, 20)

print(point.x, point.y)

# OUTPUT: '10 20'

point = POINT(y=5)

print(point.x, point.y)

# OUTPUT: '0 5'

POINT(1, 2, 3)

#
# You can, however, build much more complicated structures.
# A structure can itself contain other structures by using a structure as a field type.
#

# 
# Here is a RECT structure which contains two POINTs named upperleft and lowerright:
# 

class RECT(Structure):
        _fields_ = [("upperleft", POINT),
                    ("lowerright", POINT)]

rc = RECT(point)

print(rc.upperleft.x, rc.upperleft.y)

# OUTPUT: '0 5'

print(rc.lowerright.x, rc.lowerright.y)

# OUTPUT: '0 0'

# 
# Nested structures can also be initialized in the constructor in several ways:
# 

r = RECT(POINT(1, 2), POINT(3, 4))
r = RECT((1, 2), (3, 4))

# 
# Field descriptors can be retrieved from the class, they are useful for debugging because they can provide useful information:
# 

print(POINT.x)

# OUTPUT: '<Field type=c_long, ofs=0, size=4>'

print(POINT.y)

# OUTPUT: '<Field type=c_long, ofs=4, size=4>'
