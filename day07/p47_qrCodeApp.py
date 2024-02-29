# file : p47_qrCodeApp.py
# desc : PyQt5 QR코드앱
# > pip install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qrcode

class qtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__()
        self.initUI()

    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/qrApp.ui', self)
        self.setWindowTitle('QR코드 생성기')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널처리 
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui파일내 위젯은 자동완성X 
        self.show()

    def btnGenerateClicked(self):
        data = self.txtQrData.text()

        if len(data.strip()) == 0:
            QMessageBox.about(self, '경고', '데이터 좀 입력해라.')
            return
        else:
            imgPath = './day07/qr.png'
            qrImage = qrcode.make(data)
            qrImage.save(imgPath)
            img = QPixmap(imgPath)
            self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300)) 

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: 
            QCloseEvent.accept() # 진짜 닫음
        else:
            QCloseEvent.ignore() # 무시        

app = QApplication(sys.argv) 
inst = qtApp()
app.exec_()
