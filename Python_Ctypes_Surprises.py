# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Surprises:
# There are some edges in ctypes where you might expect something other than what actually happens.
# 

#
# Consider the following example:
# 

from ctypes import *

class POINT(Structure):
        _fields_ = ("x", c_int), ("y", c_int)

class RECT(Structure):
        _fields_ = ("a", POINT), ("b", POINT)

p1 = POINT(1, 2)
p2 = POINT(3, 4)

rc = RECT(p1, p2)

print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)

# OUTPUT: '1 2 3 4'

# now swap the two points

rc.a, rc.b = rc.b, rc.a

print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)

# OUTPUT: '3 4 3 4'

# 
# We certainly expected the last statement to print 3 4 1 2.
# What happened?
# Here are the steps of the rc.a, rc.b = rc.b, rc.a line above:
# 

temp0, temp1 = rc.b, rc.a

rc.a = temp0
rc.b = temp1

# 
# Note that temp0 and temp1 are objects still using the internal buffer of the rc object above.
# So executing rc.a = temp0 copies the buffer contents of temp0 into rc ‘s buffer. This, in turn, changes the contents of temp1.
# So, the last assignment rc.b = temp1, doesn’t have the expected effect.
# Keep in mind that retrieving sub-objects from Structure, Unions, and Arrays doesn’t copy the sub-object, instead it retrieves a wrapper object accessing
# the root-object’s underlying buffer.
#

# 
# Another example that may behave different from what one would expect is this:
# 

s = c_char_p()
s.value = "abc def ghi"

s.value

# OUTPUT: 'abc def ghi'

s.value is s.value

# OUTPUT: 'False'
