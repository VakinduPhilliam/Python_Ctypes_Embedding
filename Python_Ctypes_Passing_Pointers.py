# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Passing pointers (or: passing parameters by reference):
# Sometimes a C api function expects a pointer to a data type as parameter, probably to write into the corresponding location, or if the data is too large
# to be passed by value. This is also known as passing parameters by reference.
# ctypes exports the byref() function which is used to pass parameters by reference.
# The same effect can be achieved with the pointer() function, although pointer() does a lot more work since it constructs a real pointer object, so it is
# faster to use byref() if you don’t need the pointer object in Python itself:
# 

i = c_int()

f = c_float()

s = create_string_buffer(b'\000' * 32)

print(i.value, f.value, repr(s.value))

# OUTPUT: '0 0.0 b'''

libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
                byref(i), byref(f), s)

# OUTPUT: '3'

print(i.value, f.value, repr(s.value))

# OUTPUT: '1 3.1400001049 b'Hello''
