# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Function prototypes:
# Foreign functions can also be created by instantiating function prototypes.
# Function prototypes are similar to function prototypes in C; they describe a function (return type, argument types, calling convention) without defining
# an implementation.
# The factory functions must be called with the desired result type and the argument types of the function, and can be used as decorator factories, and as
# such, be applied to functions through the @wrapper syntax.
# 

#
# Here is the wrapping with ctypes:
# 

from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCWSTR, UINT

prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)

MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

# 
# The MessageBox foreign function can now be called in these ways:
# 

MessageBox()

MessageBox(text="Spam, spam, spam")
MessageBox(flags=2, text="foo bar")

#
# Here is the wrapping with ctypes:
# 

from ctypes import POINTER, WINFUNCTYPE, windll, WinError
from ctypes.wintypes import BOOL, HWND, RECT

prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
paramflags = (1, "hwnd"), (2, "lprect")

GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)

# 
# Functions with output parameters will automatically return the output parameter value if there is a single one, or a tuple containing the output parameter
# values when there are more than one, so the GetWindowRect function now returns a RECT instance, when called.
#

# 
# Output parameters can be combined with the errcheck protocol to do further output processing and error checking.
# The win32 GetWindowRect api function returns a BOOL to signal success or failure, so this function could do the error checking, and raises an exception
# when the api call failed:
# 

def errcheck(result, func, args):

        if not result:
            raise WinError()

        return args

GetWindowRect.errcheck = errcheck

# 
# If the errcheck function returns the argument tuple it receives unchanged, ctypes continues the normal processing it does on the output parameters.
# If you want to return a tuple of window coordinates instead of a RECT instance, you can retrieve the fields in the function and return them instead, the
# normal processing will no longer take place:
# 

def errcheck(result, func, args):

        if not result:
            raise WinError()

        rc = args[1]

        return rc.left, rc.top, rc.bottom, rc.right

GetWindowRect.errcheck = errcheck
