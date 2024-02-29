# file : p48_transApp.py
# desc : PyQt5 구글번역앱
# > pip install googletrans
# 모듈, 라이브러리 설치시 버전 업/다운, 버전을 기재해주면 됨!
# > pip install gogoletrans==3.1.0a0
# > pip install gogoletrans==4.0.0rc1

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from googletrans import Translator

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()
        self.myTrans = Translator() # 구글번역기 객체생성

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/transApp.ui', self)
        self.setWindowTitle('구글번역앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리 
        self.btnTrans.clicked.connect(self.btnTransClicked) # ui파일내 위젯은 자동완성X 
        self.txtBaseText.returnPressed.connect(self.btnTransClicked)
        self.show()

    def btnTransClicked(self):
        # QMessageBox.about(self, '번역', '번역시작!!')
        text = self.txtBaseText.text().strip()
        if len(text) != 0:
            result = self.myTrans.translate(text, src='auto', dest='en')
            self.txbResult.append(result.text)

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept() # 진짜 닫음
        else:
            QCloseEvent.ignore() # 무시        

app = QApplication(sys.argv) 
inst = qtApp()
app.exec_()
