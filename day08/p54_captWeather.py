# file : p54_captWeather.py
# desc : 네이버 날씨화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울', '강원', '대전', '대구', '부산']
# auto.mouseInfo() # 125,145
for region in regions:    
    auto.moveTo(125, 145, duration=0.5)
    auto.leftClick()
    for _ in range(5):
        auto.press('delete')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl', 'v') # 붙여넣기
    time.sleep(0.2)

    auto.press('enter') # '\n' 도 가능
    time.sleep(1.0)
    # 75,264 / 746,911

    startX, startY = 75, 264
    endX, endY = 746, 911
    # auto.screentshot() 만 사용하면 macos에서 동작안함
    im = auto.screenshot(region=(startX, startY, endX-startX, endY-startY))
    im.save(f'./day08/{region}날씨.png')
    
print('저장완료!')
