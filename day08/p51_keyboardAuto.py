# file : p51_keyboardAuto.py
# desc : 키보드 자동화 with PyAutoGui

'''
한글 입력은 pyperclip
> pip install pyperclip
'''

import pyautogui as auto
import pyperclip as clip
# auto.mouseInfo()
# auto.click(485, 591)
auto.press('enter')
auto.write("print('Hello, Python!')", interval=0.01)
auto.write("\n", interval=0.01)
auto.typewrite("print('Life is short, You need python.')", interval=0.01) # write()와 동일

# 키보드 프레스 기능
auto.press('enter'); auto.press('A')

# 키보드 단축키로 입력
# auto.hotkey('ctrl', 'a') # 전체 선택
# auto.hotkey('ctrl', 'c') # 복사
# auto.press('esc') # 선택 해제
# auto.press('\n'); auto.press('\n'); auto.press('\n')
# auto.hotkey('ctrl', 'v') # 붙여넣기
# 한글은 pyautogui에서 입력할 수 없음
clip.copy('안녕하세요. 파이썬입니다.') # 클립보드에 한글 내용을 저장
auto.hotkey('ctrl', 'v') # 붙여넣기



