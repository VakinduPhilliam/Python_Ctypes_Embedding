# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Pointers:
# Pointer instances are created by calling the pointer() function on a ctypes type:
# 

from ctypes import *

i = c_int(42)
pi = pointer(i)

# 
# Pointer instances have a contents attribute which returns the object to which the pointer points, the i object above:
# 

pi.contents

# OUTPUT: 'c_long(42)

# 
# Note that ctypes does not have OOR (original object return), it constructs a new, equivalent object each time you retrieve an attribute:
# 

pi.contents is i

# OUTPUT: 'False'

pi.contents is pi.contents

# OUTPUT: 'False'

# 
# Assigning another c_int instance to the pointer’s contents attribute would cause the pointer to point to the memory location where this is stored:
# 

i = c_int(99)

pi.contents = i
pi.contents

# OUTPUT: 'c_long(99)'

# 
# Pointer instances can also be indexed with integers:
# 

pi[0]

# OUTPUT: '99'

# 
# Assigning to an integer index changes the pointed to value:
# 

print(i)

# OUTPUT: 'c_long(99)'

pi[0] = 22
print(i)

# OUTPUT: 'c_long(22)'

# 
# It is also possible to use indexes different from 0, but you must know what you’re doing, just as in C: You can access or change arbitrary memory
# locations.
# Generally you only use this feature if you receive a pointer from a C function, and you know that the pointer actually points to an array instead of a
# single item.
#

# 
# Behind the scenes, the pointer() function does more than simply create pointer instances, it has to create pointer types first.
# This is done with the POINTER() function, which accepts any ctypes type, and returns a new type:
# 

PI = POINTER(c_int)
PI

# OUTPUT: '<class 'ctypes.LP_c_long'>'

PI(42)

PI(c_int(42))

# OUTPUT: '<ctypes.LP_c_long object at 0x...>'

# 
# Calling the pointer type without an argument creates a NULL pointer. NULL pointers have a False boolean value:
# 

null_ptr = POINTER(c_int)()

print(bool(null_ptr))

# OUTPUT: 'False'

# 
# ctypes checks for NULL when dereferencing pointers (but dereferencing invalid non-NULL pointers would crash Python):
# 

null_ptr[0]

null_ptr[0] = 1234
