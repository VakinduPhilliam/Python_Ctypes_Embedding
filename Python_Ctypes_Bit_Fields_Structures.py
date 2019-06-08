# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Bit fields in structures and unions:
# It is possible to create structures and unions containing bit fields.
# Bit fields are only possible for integer fields, the bit width is specified as the third item in the _fields_ tuples:
# 

class Int(Structure):
        _fields_ = [("first_16", c_int, 16),
                    ("second_16", c_int, 16)]

print(Int.first_16)

# OUTPUT: '<Field type=c_long, ofs=0:0, bits=16>'

print(Int.second_16)

# OUTPUT: '<Field type=c_long, ofs=0:16, bits=16>'
