# file : p74_simpleNotepad.py
# desc : 심플 노트패드 완성

import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# 리소스 파일 추가

class WinApp(QMainWindow): # QWidget이 아님!!
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        uic.loadUi('./day10/notepad.ui', self)
        self.setWindowIcon(QIcon('./day10/editor.png'))
        self.file_path = None
        self.show()

    def initSignal(self):
        # 메뉴/툴바 액션에 대한 시그널처리함수 선언...
        self.action_Open.triggered.connect(self.actionOpenClicked)
        self.action_Save.triggered.connect(self.actionSaveClicked)
        self.action_Save_as.triggered.connect(self.actionSaveAsClicked)
        self.action_Quit.triggered.connect(self.actionQuitClicked)
        self.action_About.triggered.connect(self.actionAboutClicked)

    def actionOpenClicked(self):
        global path

        path = QFileDialog.getOpenFileName(self, 'Open', '', 'text file(*.txt;*.text;*.log)')[0]
        self.title = 'test'
        if path:
            self.pteContent.setPlainText(open(path, mode='r', encoding='utf-8').read())
            self.title = path
            self.file_path = path

    def actionSaveClicked(self):
        try:
            if self.file_path is None:
                print('1')
                self.actionSaveAsClicked()
                print('2')
            else:
                with open(self.file_path, mode='w', encoding='utf-8') as f:
                    f.write(self.pteContent.toPlainText())
                self.pteContent.document().setModified(False)
                print('Saved!!')
        except:
            pass

    def actionSaveAsClicked(self):
        path = QFileDialog.getSaveFileName(self, 'Sava As', '', 'text file(*.txt;*.text;*.log)')[0]
        if path:
            self.file_path = path            
            self.actionSaveClicked()                                             

    def actionQuitClicked(self):
        exit(0)

    def actionAboutClicked(self):
        QMessageBox.about(self, '심플노트패드', '심플 노트패드 v0.1')

    def resizeEvent(self, QResizeEvent) -> None:
        self.pteContent.resize(self.geometry().width(), self.geometry().height())

    def closeEvent(self, QCloseEvent) -> None:
        re = QMessageBox.question(self, '종료', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: QCloseEvent.accept()
        else: QCloseEvent.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())