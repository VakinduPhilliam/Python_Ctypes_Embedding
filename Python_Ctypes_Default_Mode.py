# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Loading shared libraries
#

#
# ctypes.DEFAULT_MODE: 
# The default mode which is used to load shared libraries. On OSX 10.3, this is RTLD_GLOBAL, otherwise it is the same as RTLD_LOCAL.
# 

#
# Instances of these classes have no public methods. Functions exported by the shared library can be accessed as attributes or by index.
# Please note that accessing the function through an attribute caches the result and therefore accessing it repeatedly returns the same object each time.
# On the other hand, accessing it through an index returns a new object each time:
# 

from ctypes import CDLL

libc = CDLL("libc.so.6")  # On Linux
libc.time == libc.time

# OUTPUT: 'True'

libc['time'] == libc['time']

# OUTPUT: 'False'
