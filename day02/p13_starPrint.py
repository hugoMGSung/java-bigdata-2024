# file: p13_starPrint.py
# desc: 별찍기
print('예제그림 ----->> ')
for i in range(1, 6):
    print('*' * i)

# 2중 for문으로 결과를 똑같이 만드시오
print('\n')

print('별찍기 ----->> ')

for i in range(1, 6): # 손댈필요 없음
    for j in range(i, 6): # range()안쪽만 손대면 끝
        print(' ', end='')

    for j in range(6-i, 6): # 삼중for문으로 변경테스트!
        print('*', end='')
    print()

