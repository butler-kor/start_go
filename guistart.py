import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import webbrowser
import time
form_class = uic.loadUiType("radiobuttonTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox안에 있는 RadioButton들을 연결합니다.
        #GroupBox의 자세한 설명은 02.14 GroupBox를 참고하세요.
        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self) :
        if self.groupBox_rad1.isChecked() : webbrowser.open("https://www.youtube.com/@SBS_Radio")
        elif self.groupBox_rad2.isChecked() : webbrowser.open("https://www.youtube.com/watch?v=QEItfRz1fEI")
        elif self.groupBox_rad3.isChecked() : webbrowser.open("https://www.youtube.com/@KBS_1Radio")
        elif self.groupBox_rad4.isChecked() : webbrowser.open("https://www.youtube.com/@mbcradio_sisa")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()