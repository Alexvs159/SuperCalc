import sys

from window import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
operations=['+','-','*','/']
buffer_s = ''
buffer1=0
buffer2=0
oper=''
oper_history=[]

class SuperCalc(QMainWindow):

    def __init__(self):
        super(SuperCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_1.clicked.connect(self.func_1)
        self.ui.btn_2.clicked.connect(self.func_2)
        self.ui.btn_3.clicked.connect(self.func_3)
        self.ui.btn_4.clicked.connect(self.func_4)
        self.ui.btn_5.clicked.connect(self.func_5)
        self.ui.btn_6.clicked.connect(self.func_6)
        self.ui.btn_7.clicked.connect(self.func_7)
        self.ui.btn_8.clicked.connect(self.func_8)
        self.ui.btn_9.clicked.connect(self.func_9)
        self.ui.btn_0.clicked.connect(self.func_0)
        self.ui.btn_add.clicked.connect(self.func_add)
        self.ui.btn_minus.clicked.connect(self.func_minus)
        self.ui.btn_aster.clicked.connect(self.func_mult)
        self.ui.btn_div.clicked.connect(self.func_div)
    def func_1(self):
        global buffer_s
        buffer_s += '1'
        self.ui.lcd.display(buffer_s)
    def func_2(self):
        global buffer_s
        buffer_s+='2'
        self.ui.lcd.display(buffer_s)
    def func_3(self):
        global buffer_s
        buffer_s += '3'
        self.ui.lcd.display(buffer_s)
    def func_4(self):
        global buffer_s
        buffer_s += '4'
        self.ui.lcd.display(buffer_s)
    def func_5(self):
        global buffer_s
        buffer_s += '5'
        self.ui.lcd.display(buffer_s)
    def func_6(self):
        global buffer_s
        buffer_s += '6'
        self.ui.lcd.display(buffer_s)
    def func_7(self):
        global buffer_s
        buffer_s += '7'
        self.ui.lcd.display(buffer_s)
    def func_8(self):
        global buffer_s
        buffer_s += '8'
        self.ui.lcd.display(buffer_s)
    def func_9(self):
        global buffer_s
        buffer_s += '9'
        self.ui.lcd.display(buffer_s)
    def func_0(self):
        global buffer_s
        buffer_s += '0'
        self.ui.lcd.display(buffer_s)

    def func_add(self):
        global buffer_s, oper
        oper='+'
        if buffer_s!='':
            self.func_oper()
    def func_minus(self):
        global buffer_s, oper
        oper='-'
        if buffer_s!='':
            self.func_oper()
    def func_mult(self):
        global buffer_s, oper
        oper='*'
        if buffer_s!='':
            self.func_oper()
    def func_div(self):
        global buffer_s, oper
        oper='/'
        if buffer_s!='':
            self.func_oper()

    def history_display(self):
        global buffer_s
        self.ui.history.append(i)

    def func_oper(self):
        global oper, buffer_s, buffer1, buffer2
        buffer = int(buffer_s)
        if oper == '+':
            buffer1 += buffer
        if oper == '-':
            buffer1 -= buffer
        if oper == '*':
            buffer1 *= buffer
        if oper == '/':
            buffer1 /= buffer

        buffer_s = str(buffer1)
        # self.history_display()
        self.ui.lcd.display(buffer_s)
        buffer2 = buffer1
        buffer_s = ''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperCalc()
    window.show()

    sys.exit(app.exec())