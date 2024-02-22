# file: p07_variable.py
# desc: 변수에 대하여
from copy import copy

a = [1,2,3]
print(id(a))
b = a
print(id(b))

# del b[2]
# print(a)

d = copy(a)
print(id(d))
del d[2]
print(a)