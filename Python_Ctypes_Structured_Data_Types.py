# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Structured data types:
#

#
# _fields_ 
# A sequence defining the structure fields.
# The items must be 2-tuples or 3-tuples.
# The first item is the name of the field, the second item specifies the type of the field; it can be any ctypes data type.
#

# 
# For integer type fields like c_int, a third optional item can be given.
# It must be a small positive integer defining the bit width of the field.
# Field names must be unique within one structure or union. This is not checked, only one field can be accessed when names are repeated.
# It is possible to define the _fields_ class variable after the class statement that defines the Structure subclass, this allows creating data types that
# directly or indirectly reference themselves:
# 

class List(Structure):
                pass

List._fields_ = [("pnext", POINTER(List)),
                 ...
                ]


#
# _anonymous_ 
# An optional sequence that lists the names of unnamed (anonymous) fields.
# _anonymous_ must be already defined when _fields_ is assigned, otherwise it will have no effect.
#

# 
# The fields listed in this variable must be structure or union type fields. ctypes will create descriptors in the structure type that allows accessing the
# nested fields directly, without the need to create the structure or union field.
#

# 
# Here is an example type (Windows):
# 

class _U(Union):

    _fields_ = [("lptdesc", POINTER(TYPEDESC)),
                ("lpadesc", POINTER(ARRAYDESC)),
                ("hreftype", HREFTYPE)]

class TYPEDESC(Structure):

    _anonymous_ = ("u",)

    _fields_ = [("u", _U),
                ("vt", VARTYPE)]

#
# The TYPEDESC structure describes a COM data type, the vt field specifies which one of the union fields is valid. Since the u field is defined as anonymous
# field, it is now possible to access the members directly off the TYPEDESC instance.
# td.lptdesc and td.u.lptdesc are equivalent, but the former is faster since it does not need to create a temporary union instance:
# 

td = TYPEDESC()

td.vt = VT_PTR
td.lptdesc = POINTER(some_type)

td.u.lptdesc = POINTER(some_type)
