# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Type conversions:
# Usually, ctypes does strict type checking.
# This means, if you have POINTER(c_int) in the argtypes list of a function or as the type of a member field in a structure definition, only instances of
# exactly the same type are accepted.
# There are some exceptions to this rule, where ctypes accepts other objects.
# For example, you can pass compatible array instances instead of pointer types. So, for POINTER(c_int), ctypes accepts an array of c_int:
# 

class Bar(Structure):
        _fields_ = [("count", c_int), ("values", POINTER(c_int))]

bar = Bar()
bar.values = (c_int * 3)(1, 2, 3)

bar.count = 3

for i in range(bar.count):
        print(bar.values[i])

#
# OUTPUT:
#
# 1
# 2
# 3

# 
# In addition, if a function argument is explicitly declared to be a pointer type (such as POINTER(c_int)) in argtypes, an object of the pointed type
# (c_int in this case) can be passed to the function.
# ctypes will apply the required byref() conversion in this case automatically.
#

# 
# To set a POINTER type field to NULL, you can assign None:
# 

bar.values = None

# 
# Sometimes you have instances of incompatible types.
# In C, you can cast one type into another type.
# ctypes provides a cast() function which can be used in the same way.
# The Bar structure defined above accepts POINTER(c_int) pointers or c_int arrays for its values field, but not instances of other types:
# 

bar.values = (c_byte * 4)()

# 
# For these cases, the cast() function is handy.
# 
# The cast() function can be used to cast a ctypes instance into a pointer to a different ctypes data type.
# cast() takes two parameters, a ctypes object that is or can be converted to a pointer of some kind, and a ctypes pointer type.
# It returns an instance of the second argument, which references the same memory block as the first argument:
# 

a = (c_byte * 4)()

cast(a, POINTER(c_int))

# OUTPUT: '<ctypes.LP_c_long object at ...>'
 
#
# So, cast() can be used to assign to the values field of Bar the structure:
# 

bar = Bar()
bar.values = cast((c_byte * 4)(), POINTER(c_int))

print(bar.values[0])

# OUTPUT: '0'
