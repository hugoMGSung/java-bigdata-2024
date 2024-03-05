# file : p63_opencv.py
# desc : OpenCV 영상처리

import cv2

samplePath = './day09/earth.mp4'
cap = cv2.VideoCapture(samplePath) # 0은 웹캠 또는 문자열로 동영상 경로

while True:
    ret, frame = cap.read()

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue

    ## 영상 편집
    blur = cv2.blur(frame, (10,10))
    flip = cv2.flip(frame, 0)

    cv2.imshow('original', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('flop', flip)

    key = cv2.waitKey(5) # 5ms 딜레이 
    if key == ord('q'): # esc=27, q=ord('q')         
        break
    elif key == ord('c'): # 화면캡처
        cv2.imwrite('./day09/capt.jpg', frame)

cap.release() 
cv2.destroyAllWindows()