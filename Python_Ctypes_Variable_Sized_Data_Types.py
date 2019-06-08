# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Variable-sized data types:
# ctypes provides some support for variable-sized arrays and structures.
#

# 
# The resize() function can be used to resize the memory buffer of an existing ctypes object.
# The function takes the object as first argument, and the requested size in bytes as the second argument.
# The memory block cannot be made smaller than the natural memory block specified by the objects type, a ValueError is raised if this is tried:
# 

short_array = (c_short * 4)()

print(sizeof(short_array))

# OUTPUT: '8'

resize(short_array, 4)
resize(short_array, 32)

sizeof(short_array)

# OUTPUT: '32'

sizeof(type(short_array))

# OUTPUT: '8'
 
#
# This is nice and fine, but how would one access the additional elements contained in this array?
# Since the type still only knows about 4 elements, we get errors accessing other elements:
# 

short_array[:]

# OUTPUT: '[0, 0, 0, 0]'

short_array[7]
