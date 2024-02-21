# file : p04_list.py
# desc : 리스트, 튜플

## 파이썬엔 배열이 없다. 리스트로 대신함
even = [2,4,6,8,10]
odd = [1,3,5,7,9]

print(even)
print(even[4]) # 길이가 n일때 마지막 인덱스는 n-1

even[4] = 20
print(even) # 리스트는 인덱스의 값을 변경가능

datas = [123, 45.6, True, 'Hello', odd, None] # 형지정 없기때문에 어떤자료형이든 다 리스트에 할당가능
print(datas)

## 인덱싱, 슬라이싱
print(odd[2])
print(even[0] + odd[0])

cpWords = ['Life', 'is', 'short']
print(cpWords[0] + cpWords[2])

print(even[1:4]) # [4,6,8]

## 2차원 리스트
# 3행 4열
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12]]

d2Datas = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

for i in d2Datas:
    print(i)

dm1col1 = [1,2,3,4]
dm1col2 = [5,6,7,8]
dm1col3 = [9,10,11,12]

print([dm1col1, dm1col2, dm1col3])
# 리스트 연산은 문자열 연산과 동일
print(even + odd)
print(odd * 2)

## 값 변경
even[3] = 10
print(even)

del even[2] # 삭제
print(even)

## 리스트 함수
# append 리스트 제일 뒤에 추가
even.append(30)
print(even)

# insert 원하는 위치 값 추가
even.insert(2, 6) # 인덱스 2에다가 6을 추가
print(even)

# 정렬
origin = [45, 23, 9, 17, 1, 5, 11, 3, 29, 30]

origin.sort() # 오름차순(Ascending)
print(origin)
origin.sort(reverse=True) # 내림차순(Descending)
print(origin)

# 뒤집기
aa = ['a', 'f', 'e', 'b']
aa.reverse()

print(aa)

print(aa.count('a'))
print(aa.index('e'))

bb = [1, 3, 5, 6, 8, 3, 1]
bb.remove(3) # 맨 앞에 있는 3만 지움

print(bb)

print(even.pop())
print(even.pop()) # 스택의 기능 append() 마지막에 할당, pop() 마지막에서 값 꺼내기
print(even)

## 튜플
# 리스트랑 동일, 단, 삭제,편집 불가
tVal = (1, 3, 5, 7, 9)

# tVal[2] = 11 # 튜플은 한번 만들어지면 끝까지 그대로 사용해야
# del tVal[2]