# file: p15_function.py
# desc: 함수 학습

def plus(a, b): # 매개변수, 리턴값O
    res = a + b
    return res

def minus(a, b): # 매개변수, 리턴값X
    res = a - b
    print(res)

def multi(): # 매개변수X, 리턴값O
    global a, c # 밖에 있는 전역변수 a, c를 사용하겠다 
    res = a * c
    return res

def divide():
    global a, c
    print(a / c)

def pow(a=2, b=10): # 기본인수를 지정할때는 뒤에서부터
    res = a ** b
    return res

print('더하기')
a = 10
c = 7
result = plus(a, c)
print(result)

minus(a, c)
result = multi()
print(result)
divide()

print(pow()) # 기본인수

def plus_many(*items): # 동적 매개변수
    result = 0
    for item in items:
        result += item
    
    return result

print(plus_many(1, 2))
print(plus_many(1, 2, 3))
print(plus_many(1, 2, 3, 4, 5))
print(plus_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calcurator(mode, *args): #
    if mode == 'a': # 더하기
        result = 0
        for i in args:
            result += i

    elif mode == 'n': # 빼기
        result = args[0]
        for i in args[1:]:
            result -= i

    elif mode == 'm': # 곱하기
        result = 1
        for i in args:
            result *= i

    elif mode == 'd': # 나누기
        result = args[0]
        for i in args[1:]:
            result /= i

    return result

print(calcurator('a', 1,2,3,4,5,6,7,8,9,10,11)) # 66
print(calcurator('n', 100, 10, 5, 5, 4)) # 76
print(calcurator('m', 2, 2, 2, 2, 2)) # 32
print(calcurator('d', 100, 5, 4, 5)) # 1.0


def print_kwargs(**items): # 키워드 매개변수. 딕셔너리를 생성
    print(items)

print_kwargs(name='Peter parker', age=18, weapon='web shooter')

# 리턴을 한번에 여러개(두개 이상) 리턴할 수 있음. 튜플로 리턴한다
def calc2(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    res4 = a / b

    return (res1, res2, res3, res4)

a, b, c, d = calc2(3, 4)

print(a, b, c, d)

## 익명함수 람다함수
add = lambda a, b: a+b # 람다함수 끝
print(add(5,4))