# file : p55_katalkAuto.py
# desc : 카톡PC에서 자동으로 메시지보내기
#        pyautogui.ImageNotFoundException 예외 자주발생

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.click(clickPos)    
time.sleep(0.5)

groupLoc = auto.locateOnScreen('./day08/findLoc2.png')
clickPos = auto.center(groupLoc)
auto.doubleClick(clickPos)
time.sleep(0.2)

clip.copy('자동으로 보내는 메시지. 자주 하지마세요~')
auto.hotkey('ctrl', 'v')
auto.press('\n')