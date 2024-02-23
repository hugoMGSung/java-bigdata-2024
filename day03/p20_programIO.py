# file : p20_programIO.py
# desc : 프로그램 입출력, 프로그램으로 명령 실행시 파라미터를 받을 수 있음

import sys

args = sys.argv[1:] 
for i in args:
    # print(i, end=' / ')
    if i == '--version':
        print('Python 3.12.2')
    elif i == '-h':
        print('도움말 >> ')
    else:
        print('재입력')
        
    break