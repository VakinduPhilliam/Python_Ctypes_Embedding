# Python Ctypes
# ctypes — A foreign function library for Python.
# It provides C compatible data types, and allows calling functions in DLLs or shared libraries.
# It can be used to wrap these libraries in pure Python.
#

#
# Incomplete Types:
# Incomplete Types are structures, unions or arrays whose members are not yet specified.
# In C, they are specified by forward declarations, which are defined later:
# 

# struct cell; /* forward declaration */
#
# struct cell {
#    char *name;
#    struct cell *next;
# };
#

# 
# The straightforward translation into ctypes code would be this, but it does not work:
# 

class cell(Structure):
        _fields_ = [("name", c_char_p),
                    ("next", POINTER(cell))]

# 
# because the new class cell is not available in the class statement itself.
# In ctypes, we can define the cell class and set the _fields_ attribute later, after the class statement:
# 

from ctypes import *

class cell(Structure):
              pass

cell._fields_ = [("name", c_char_p),
                     ("next", POINTER(cell))]

# 
# Lets try it. We create two instances of cell, and let them point to each other, and finally follow the pointer chain a few times:
# 

c1 = cell()
c1.name = "foo"

c2 = cell()
c2.name = "bar"

c1.next = pointer(c2)
c2.next = pointer(c1)

p = c1

for i in range(8):
        print(p.name, end=" ")

        p = p.next[0]

# OUTPUT: 'foo bar foo bar foo bar foo bar'
