import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import quiz
import random


form_class = uic.loadUiType("weather2_ui.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        quiz_text, answer_text = quiz.quiz()
        self.correct_answer = answer_text
        options = weather2_data.wrong_answer() + [self.correct_answer]
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
#
