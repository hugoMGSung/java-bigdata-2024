# file : p35_qtApp.py
# desc : PyQt5 앱 만들기
'''
PyQt5 -> Qt를 파이썬에서 쓸수 있도록 만든 라이브러리
Qt -> C,C++ 사용할 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
# QApplication 만들앱 전체 관리 클래스, QWidget 메뉴가 없는 윈도앱, QMainWindow 메뉴가 있는 윈도앱
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow  

class qtApp(QWidget):  # QWidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() # 생성자, 부모클래스의 생성자 함수도 실행되어야
        self.initUI();

    def initUI(self):
        self.setGeometry(300, 300, 800, 400) # 바탕화면 정해진 위치에 넓이와 높이로 그릴 설정
        self.setWindowTitle('첫번째 윈도우앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.show() # 윈도창 그려!

    def paintEvent(self, event) -> None:
        paint = QPainter() # 윈도창 위에 그림그리는 객체
        paint.begin(self) # 그림을 그리기 시작하면
        paint.setPen(QColor(200, 0, 0)) # dark red
        paint.setFont(QFont('Bauhaus 93', 40))  # 'NanumGothicCoding'
        paint.drawText(250, 400//2, 'Hello PyQt!')
        paint.end() # 반드시 닫아야 함

app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실행
