# file: p08_review.py
# desc: 리뷰

## Q2
a = 13 
print('a는 ', end='')
if a % 2 ==0:
    print('짝수')
else:
    print('홀수')

## Q3
pin = '881120-1068234'
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

## Q5
a = 'a:b:c:d'
b = a.replace(':', '#')
print(b) # a#b#c#d

## Q6
a = [1,3,5,4,2]
a.sort()
a.sort(reverse=True)
print(a)

## Q10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # {'A':90, 'C':70}
print(result) # 80