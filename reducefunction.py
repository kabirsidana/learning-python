# Reduce Function (only give result as single argument , reduce the result)
from functools import reduce
"""
lst=[1,2,3,46,7,8,34,34]
a=reduce(lambda x,y:x+y,lst)
print(a)
"""
lst=[1,2,3,4,5,6,7,8]
a=reduce(lambda x,y:x*y,lst)
print(a)