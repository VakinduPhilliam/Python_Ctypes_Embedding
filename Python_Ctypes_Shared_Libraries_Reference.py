# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# ctypes reference:
# Finding shared libraries
#

#
# ctypes.util.find_library(name). 
# Try to find a library and return a pathname.
# name is the library name without any prefix like lib, suffix like .so, .dylib or version number (this is the form used for the posix linker option -l).
# If no library can be found, returns None.
#

# 
# The exact functionality is system dependent.
# On Linux, find_library() tries to run external programs (/sbin/ldconfig, gcc, objdump and ld) to find the library file.
# It returns the filename of the library file.
# 

#
# On Linux, the value of the environment variable LD_LIBRARY_PATH is used when searching for libraries, if a library cannot be found by any other means.
# 

#
# Here are some examples:
# 

from ctypes.util import find_library

find_library("m")

# OUTPUT: 'libm.so.6'

find_library("c")

# OUTPUT: 'libc.so.6'

find_library("bz2")

# OUTPUT: 'libbz2.so.1.0'

# 
# On OS X, find_library() tries several predefined naming schemes and paths to locate the library, and returns a full pathname if successful:
# 

from ctypes.util import find_library

find_library("c")

# OUTPUT: '/usr/lib/libc.dylib'

find_library("m")

# OUTPUT: '/usr/lib/libm.dylib'

find_library("bz2")

# OUTPUT: '/usr/lib/libbz2.dylib'

find_library("AGL")

# OUTPUT: '/System/Library/Frameworks/AGL.framework/AGL'
