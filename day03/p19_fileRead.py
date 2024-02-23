# file : p19_fileRead.py
# desc : 텍스트 파일 읽기 

f = open('./day03/CHANGELOG.md', mode='r', encoding='utf-8')

while True:
    read = f.readline() # 한줄씩
    if not read: break # 더이상 읽을 값이 없으면 반복문 탈출    
    print(read.replace('\n', ''))

f.close()