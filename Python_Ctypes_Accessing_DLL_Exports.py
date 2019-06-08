# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Accessing values exported from dlls:
# Some shared libraries not only export functions, they also export variables.
# An example in the Python library itself is the Py_OptimizeFlag, an integer set to 0, 1, or 2, depending on the -O or -OO flag given on startup.
# ctypes can access values like this with the in_dll() class methods of the type.
# pythonapi is a predefined symbol giving access to the Python C api:
# 

opt_flag = c_int.in_dll(pythonapi, "Py_OptimizeFlag")

print(opt_flag)

# OUTPUT: 'c_long(0)'
 
#
# If the interpreter would have been started with -O, the sample would have printed c_long(1), or c_long(2) if -OO would have been specified.
# An extended example which also demonstrates the use of pointers accesses the PyImport_FrozenModules pointer exported by Python.
#

# 
# Quoting the docs for that value:
# 
# This pointer is initialized to point to an array of struct _frozen records, terminated by one whose members are all NULL or zero.
# When a frozen module is imported, it is searched in this table.
# Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.
#
# So manipulating this pointer could even prove useful.
# To restrict the example size, we show only how this table can be read with ctypes:
# 

from ctypes import *

class struct_frozen(Structure):
       _fields_ = [("name", c_char_p),
                    ("code", POINTER(c_ubyte)),
                    ("size", c_int)]

# 
# We have defined the struct _frozen data type, so we can get the pointer to the table:
# 

FrozenTable = POINTER(struct_frozen)
table = FrozenTable.in_dll(pythonapi, "PyImport_FrozenModules")

# 
# Since table is a pointer to the array of struct_frozen records, we can iterate over it, but we just have to make sure that our loop terminates, because
# pointers have no size.
# Sooner or later it would probably crash with an access violation or whatever, so it’s better to break out of the loop when we hit the NULL entry:
# 

for item in table:

        if item.name is None:
            break

        print(item.name.decode("ascii"), item.size)


