# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Fundamental data types
# ctypes defines a number of primitive C compatible data types:
#

#
# The constructor accepts any object with a truth value.
# All these types can be created by calling them with an optional initializer of the correct type and value:
# 

c_int()

# OUTPUT: 'c_long(0)'

c_wchar_p("Hello, World")

# OUTPUT: 'c_wchar_p(140018365411392)'

c_ushort(-3)

# OUTPUT: 'c_ushort(65533)'

# 
# Since these types are mutable, their value can also be changed afterwards:
# 

i = c_int(42)
print(i)

# OUTPUT: 'c_long(42)'

print(i.value)

# OUTPUT: '42'

i.value = -99
print(i.value)

# OUTPUT: '-99'

# 
# Assigning a new value to instances of the pointer types c_char_p, c_wchar_p, and c_void_p changes the memory location they point to, not the contents of
# the memory block (of course not, because Python bytes objects are immutable):
# 

s = "Hello, World"
c_s = c_wchar_p(s)

print(c_s)

# OUTPUT: 'c_wchar_p(139966785747344)'

print(c_s.value)

# OUTPUT: 'Hello World'

c_s.value = "Hi, there"
print(c_s)              # the memory location has changed

# OUTPUT: 'c_wchar_p(139966783348904)'

print(c_s.value)

# OUTPUT: 'Hi, there'

print(s)                # first object is unchanged

# OUTPUT: 'Hello, World'

#
# You should be careful, however, not to pass them to functions expecting pointers to mutable memory.
# If you need mutable memory blocks, ctypes has a create_string_buffer() function which creates these in various ways.
# The current memory block contents can be accessed (or changed) with the raw property; if you want to access it as NUL terminated string, use the value
# property:
# 

from ctypes import *

p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
print(sizeof(p), repr(p.raw))

# OUTPUT: '3 b'\x00\x00\x00''

p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
print(sizeof(p), repr(p.raw))

# OUTPUT: '6 b'Hello\x00''

print(repr(p.value))

# OUTPUT: 'b'Hello''

p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
print(sizeof(p), repr(p.raw))

# OUTPUT: '10 b'Hello\x00\x00\x00\x00\x00''

p.value = b"Hi"
print(sizeof(p), repr(p.raw))

# OUTPUT: '10 b'Hi\x00lo\x00\x00\x00\x00\x00''

#
# The create_string_buffer() function replaces the c_buffer() function (which is still available as an alias), as well as the c_string() function from
# earlier ctypes releases.
# To create a mutable memory block containing unicode characters of the C type wchar_t use the create_unicode_buffer() function.
#
