import sys

from window import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
isbuffer=False
wasequal=False
buffer_s = ''
buffer1=''
buffer2=0
labeltext=[]

class SuperCalc(QMainWindow):

    def __init__(self):
        super(SuperCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
# Привязка кнопок к функциям
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
        self.ui.btn_calc.clicked.connect(self.func_equal)
#Функции кнопок
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
        else:
             labelstr=''
             labeltext[-1] = oper
             for i in labeltext:
                 labelstr += i + ' '
             self.ui.label.setText(labelstr)
    def func_minus(self):
        global buffer_s, oper, labeltext
        oper='-'
        if buffer_s!='':
            self.func_oper()
        else:
             labelstr=''
             labeltext[-1] = oper
             for i in labeltext:
                 labelstr += i + ' '
             self.ui.label.setText(labelstr)
    def func_mult(self):
        global buffer_s, oper
        oper='*'
        if buffer_s!='':
            self.func_oper()
        else:
             labelstr=''
             labeltext[-1] = oper
             for i in labeltext:
                 labelstr += i + ' '
             self.ui.label.setText(labelstr)
    def func_div(self):
        global oper
        oper='/'
        if buffer_s!='':
            self.func_oper()
        else:
             labelstr=''
             labeltext[-1] = oper
             for i in labeltext:
                 labelstr += i + ' '
             self.ui.label.setText(labelstr)

    def func_equal(self):
        global oper, buffer_s, buffer1, buffer2, isbuffer, labeltext, wasequal
        if not wasequal and isbuffer:
            if float(int(buffer_s))<float(buffer_s):  # проверяем, float или int
                buffer = float(buffer_s)
            else:
                buffer = int(buffer_s)
            if oper == '+':
                buffer1 += buffer
            if oper == '-':
                buffer1 -= buffer
            if oper == '*':
                buffer1 *= buffer
            if oper == '/':
                buffer1 /= buffer
                buffer2=buffer1
        elif wasequal:
            print (oper)
            print (buffer1)
            print (buffer2)
            if oper == '+':
                buffer2 += buffer1
            if oper == '-':
                buffer2 -= buffer1
            if oper == '*':
                buffer2 *= buffer1
            if oper == '/':
                buffer2 /= buffer1
            labeltext.append(str(buffer1))
            buffer_s=str(buffer2)
        self.ui.lcd.display(buffer1)
        labeltext.append(buffer_s)
        labeltext.append(oper)
        labelstr = ''
        for i in labeltext:
            labelstr += i + ' '
        self.ui.label.setText(labelstr)
        buffer_s = ''
        isbuffer = True
        wasequal = True





    def func_oper(self):
        global oper, buffer_s, buffer1, buffer2, isbuffer, labeltext
        if isbuffer:  # Проверяем наличие числа в буфере
            if float(int(buffer_s))<float(buffer_s):  # проверяем, float или int
                buffer = float(buffer_s)
            else:
                buffer = int(buffer_s)
            if oper == '+':
                buffer1 += buffer
            if oper == '-':
                buffer1 -= buffer
            if oper == '*':
                buffer1 *= buffer
            if oper == '/':
                buffer1 /= buffer
        else:
            if float(int(buffer_s))<float(buffer_s):
                buffer1 = float(buffer_s)
            else:
                buffer1 = int(buffer_s)
        # buffer_s = str(buffer1)
        # self.history_display()
        self.ui.lcd.display(buffer1)
        labeltext.append(buffer_s)
        labeltext.append(oper)
        labelstr=''
        for i in labeltext:
            labelstr+=i+' '
        self.ui.label.setText(labelstr)
        buffer_s = ''
        buffer2=buffer1
        isbuffer=True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperCalc()
    window.show()

    sys.exit(app.exec())