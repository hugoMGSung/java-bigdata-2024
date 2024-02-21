# file: p03_string.py
# desc: 문자열 자료형과 연산

a = "Hello World"
print(a)
b = 'Hello World'
print(b)
c = "Hello, \'Ashley\'"
print(c)
# 탈출문자 \n, \t 외 나머지는 파이썬에 잘 사용되지 않음

# 문장을 여러줄 쓰고 싶으면 \로...
d = 'Hello~\n' \
'I\'m Hugo.' \
'Nice to meet you'
print(d)
# 여러줄 문장을 쓸때는 ''',  """
d = '''Hello~
    I'm Ashley.
    Nict to meet you, too.'''
print(d)

## 문자열 연산 +, *
before = 'I wanna go to '
after = 'Boracai! '
print(before + after) # +는 문자열을 합쳐서 하나의 문자열 만듬
print(after * 3) # * 문자열을 몇번 반복

## 문자열 길이구하기
print('글자길이 =',len(before))
print('한글글자길이', len('안녕하세요')) # 5

## 문자열 인덱싱, 슬라이싱
cp = 'Life is too short, You need Python'
print(len(cp))

## 슬라이싱
print(cp[8])
print(cp[17])

# cp[8] = 'd' # 문자열은 배열이긴 하지만 값을 변경X
# 문자열 범위 슬라이싱
print(cp[12:16+1]) # : 뒤에 있는 숫자는 항상 +1

print(ascii('안'), ascii('녕'), ascii('하'), ascii('세'), ascii('요'))
print(chr(97)) 

# 기존 문자열로 새로운 문자열을 만들때는 슬라이싱, 다른 문자열로 대체필수
print(cp[0:7], 'long', cp[17:]) # : 뒤에 생략하면 끝까지
# 다른언어에는 없는 - 슬라이싱
print(cp[-6:])
print(cp[-11:-7]) # -로 슬라이싱때도 :뒤에는 +1을 해줘야 함

## 문자열 포맷팅(format string)
## 파이썬에서는 %d, %s, %c 등 포맷스트링용 연산자를 사용 빈도 낮음
temp = 21
print('현재 온도는 %d도 입니다' % temp)
temp = 17 
print('현재 온도는 %d도 입니다' % temp)

## format 함수로 포맷팅(가장 일반적)
print('현재 온도는 {0}도 입니다'.format(temp))

## 날짜를 포맷으로 만들때
month = 2
day = 21
hour = 3
mins = 18
print('오늘은 {0:02d}-{1:02d}, {2:02d}:{3:02d}입니다'.format(month, day, hour, mins))

# 숫자 자료형
income = 6_000_000_000 # 연매출
print('올해 매출액은 {0:,d}원'.format(income))
PI = 3.1415926536
print('파이는 {0:10.2f}'.format(PI)) # 10.2f 소수점 .까지 다 포함해서 10자리, 소수점뒤는 2자리
# print('{0:d}'.format(PI)) # 실수형은 d(정수형 포맷팅) 불가

## f 포맷팅 3.6(2016)이후에 나온 최신방식
name = '홍길동'
age = 30

cont = f'나는 {name}이고, 나이는 {age}세 입니다.'
print(cont)
name = '성명건'
age = 47
print(f'나는 {name:>10}이고, 나이는 {age:03d}세 입니다.')
print(f'나는 {name:<10}이고, 나이는 {age:03.1f}세 입니다.') 
# 정수는 f포맷 사용가능, 실수는 d포맷 사용불가

## 문자열 함수
a = 'Life is short, You need Python'

print(a.count('Life')) # 1
print(a.count('o')) # 3

print(a.find('sh')) # 8

print(a.index('t')) # 첫번째 t의 위치 12
print(a.count('K')) # index()는 count()로 갯수가 0이 아닐때만 호출
print(','.join('abcde')) # 재밌는 함수

print(a.upper()) # 대문자
print(a.lower()) # 소문자
print(a.capitalize())  # 문장이 시작되는 첫번째 단어의 첫글자만 대문자

origin = '          H  i          '
print(f'++{origin}++')
print(f'++{origin.lstrip()}++') # 왼쪽 공백 없애버려
print(f'++{origin.rstrip()}++') # 오른쪽 공백
print(f'++{origin.strip()}++') # 양쪽 공백 다

print(cp.replace('too', '').replace(' short', 'long'))

## 문자열 자르기 -> 리스트(파이썬에는 배열X)
cpWords = cp.split(' ')
print(cpWords)