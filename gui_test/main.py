# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# import webbrowser
# import quiz
# form_class = uic.loadUiType("main.ui")[0]
#
# # 퀴즈를 입력하고
# # 답을 입력하고 (4지선다)
# # 정답이면 링크로 연결된 곳에서 정답이라고 뜨고 다른 문제가 등장
# # 오답이면 다른 사이트로 이동하고 오답이라고 뜸
#
#
#
#
#
# class WindowClass(QMainWindow, form_class) :
#     def __init__(self) :
#         super().__init__()
#         self.setupUi(self)
#
#         quiz_text, answer_text = quiz.quiz()
#
#         wa2 = quiz.wrong_answer()
#         self.quiz.setText(quiz_text)
#         self.quiz.groupBox_rad1.setText(wa2[0])
#         self.quiz.groupBox_rad2.setText(wa2[1])
#         self.quiz.groupBox_rad3.setText(wa2[2])
#         self.quiz.groupBox_rad4.setText(wa2[3])
#
#         self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
#         self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
#         self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
#         self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)
#         self.btn_1.clicked.connect(self.button1Function)
#
#     def groupboxRadFunction(self):
#         if self.groupBox_rad1.ischecked():
#             print("GroupBox_rad1 Checked")
#         elif self.groupBox_rad2.ischecked():
#             print("GroupBox_rad2 Checked")
#         elif self.groupBox_rad3.ischecked():
#             print("GroupBox_rad3 Checked")
#         elif self.groupBox_rad4.ischecked():
#             print("GroupBox_rad4 Checked")
#
#     def button1Function(self):
#             print("btn_1 Clicked")
#
#
#
# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     myWindow = WindowClass()
#     myWindow.show()
#     app.exec_()
#

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import quiz
import random


form_class = uic.loadUiType("main.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        quiz_text, answer_text = quiz.quiz()
        self.correct_answer = answer_text
        options = quiz.wrong_answer() + [self.correct_answer]
        random.shuffle(options)


        self.quiz.setText(quiz_text)
        self.groupBox_rad1.setText(options[0])
        self.groupBox_rad2.setText(options[1])
        self.groupBox_rad3.setText(options[2])
        self.groupBox_rad4.setText(options[3])
        self.btn_1.clicked.connect(self.button1Function)

    def button1Function(self):
        selected = None
        if self.groupBox_rad1.isChecked():
            selected = self.groupBox_rad1.text()
        elif self.groupBox_rad2.isChecked():
            selected = self.groupBox_rad2.text()
        elif self.groupBox_rad3.isChecked():
            selected = self.groupBox_rad3.text()
        elif self.groupBox_rad4.isChecked():
            selected = self.groupBox_rad4.text()

        if not selected:
            QMessageBox.warning(self, "선택 안 함", "먼저 답을 선택하세요.")
            return


        quiz.check_answer(self.correct_answer, selected)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())

