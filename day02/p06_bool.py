# file: p06_bool.py
# desc: 불타입, None타입 학습

# 참/거짓

a = True # true
b = False # false

print(a)
print(type(a)) # <class 'bool'>
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('Hi')) # <class 'str'>
print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'>

print(a == b)
print(a == (not b))

print(bool('H'))
# 참/거짓 구분 빈값,0,None False 그외 True

# None 타입
None

c = None
a = 1
b = 0
print(c)
print(a + b) # a True(1) False(0)

print(c + a)

