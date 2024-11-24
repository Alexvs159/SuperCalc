import sys

from window import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

class SuperCalc(QMainWindow):

    def __init__(self):
        super(SuperCalc, self).__init__()
        self.isbuffer = False
        self.buffer_s = ''
        self.buffer1 = ''
        self.buffer2 = 0
        self.labeltext = []
        self.lastoper=''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Привязка кнопок к функциям
        self.ui.btn_1.clicked.connect(lambda: self.func_number(1))
        self.ui.btn_2.clicked.connect(lambda: self.func_number(2))
        self.ui.btn_3.clicked.connect(lambda: self.func_number(3))
        self.ui.btn_4.clicked.connect(lambda: self.func_number(4))
        self.ui.btn_5.clicked.connect(lambda: self.func_number(5))
        self.ui.btn_6.clicked.connect(lambda: self.func_number(6))
        self.ui.btn_7.clicked.connect(lambda: self.func_number(7))
        self.ui.btn_8.clicked.connect(lambda: self.func_number(8))
        self.ui.btn_9.clicked.connect(lambda: self.func_number(9))
        self.ui.btn_0.clicked.connect(lambda: self.func_number(0))
        self.ui.btn_add.clicked.connect(lambda: self.func_btn_oper('+'))
        self.ui.btn_minus.clicked.connect(lambda: self.func_btn_oper('-'))
        self.ui.btn_aster.clicked.connect(lambda: self.func_btn_oper('*'))
        self.ui.btn_div.clicked.connect(lambda: self.func_btn_oper('/'))
        self.ui.btn_calc.clicked.connect(self.func_equal)
        self.ui.btn_c.clicked.connect(self.func_clear)
        self.ui.btn_backspace.clicked.connect(self.func_backspace)
        self.ui.btn_zpt.clicked.connect(self.func_zpt)
        self.ui.btn_rev.clicked.connect(self.func_rev)
        self.ui.btn_percent.clicked.connect(self.func_percent)

    # Функция кнопок с цифрами
    def func_number(self, number):
        self.buffer_s += str(number)
        self.ui.lcd.display(self.buffer_s)

    # Функция кнопок операций +-*/
    def func_btn_oper(self, oper):
        if self.buffer_s != '':

            self.func_oper(oper)
        else:
            labelstr = ''
            self.labeltext[-1] = oper
            for i in self.labeltext:
                labelstr += i + ' '
            self.ui.label.setText(labelstr)


    def func_equal(self):
        #global oper, buffer_s, buffer1, buffer2, isbuffer, labeltext
        if self.isbuffer and self.buffer_s != '':
            # if self.func_isfloat(self.buffer_s):
            #     buffer = float(self.buffer_s)
            # else:
            buffer = self.func_isfloat(self.buffer_s)
            self.buffer2 = buffer
            if self.lastoper == '+':
                self.buffer1 += buffer
            if self.lastoper == '-':
                self.buffer1 -= buffer
            if self.lastoper == '*':
                self. buffer1 *= buffer
            if self.lastoper == '/':
                self.buffer1 /= buffer

            self.isbuffer = False
            self.buffer_s = str(self.buffer1)
            self.ui.lcd.display(self.buffer_s)
            self.labeltext.append(str(self.buffer2))
            self.labeltext.append(self.lastoper)
            labelstr = ''
            for i in self.labeltext[0:-1]:
                labelstr += i + ' '
            self.ui.label.setText(labelstr)

        elif not self.isbuffer and self.buffer1 != '':
            if self.lastoper == '+':
                self.buffer1 += self.buffer2
            if self.lastoper == '-':
                self.buffer1 -= self.buffer2
            if self.lastoper == '*':
                self.buffer1 *= self.buffer2
            if self.lastoper == '/':
                self.buffer1 /= self.buffer2
            self.buffer_s = str(self.buffer1)
            self.ui.lcd.display(self.buffer_s)
            self.labeltext.append(str(self.buffer1))
            self.labeltext.append(self.lastoper)
            labelstr = ''
            for i in self.labeltext[0:-2]:
                labelstr += i + ' '
            self.ui.label.setText(labelstr)

    def func_oper_new(self, oper):
        self.lastoper = oper
        if self.isbuffer:  # Проверяем наличие числа в буфере
            if self.func_isfloat(self.buffer_s): # Проверяем дробное или целое число
                buffer = float(self.buffer_s)
            else:
                buffer = int(self.buffer_s)
            if oper == '+':
                self.buffer1 += buffer
            if oper == '-':
                self.buffer1 -= buffer
            if oper == '*':
                self.buffer1 *= buffer
            if oper == '/':
                self.buffer1 /= buffer
        else:
            if self.func_isfloat(self.buffer_s):
                self.buffer1 = float(self.buffer_s)
            else:
                 self.buffer1 = int(self.buffer_s)
            self.isbuffer = True
        self.ui.lcd.display(self.buffer1)
        self.labeltext.append(self.buffer_s)
        self.labeltext.append(oper)
        labelstr = ''
        for i in self.labeltext:
            labelstr += i + ' '
        self.ui.label.setText(labelstr)
        self.buffer_s = ''

    def func_oper(self, oper):
        self.lastoper = oper
        if self.isbuffer:  # Проверяем наличие числа в буфере
            #if self.func_isfloat(self.buffer_s): # Проверяем дробное или целое число
            #    buffer = float(self.buffer_s)
            #else:
            buffer = self.func_isfloat(self.buffer_s)
            if oper == '+':
                self.buffer1 += buffer
            if oper == '-':
                self.buffer1 -= buffer
            if oper == '*':
                self.buffer1 *= buffer
            if oper == '/':
                self.buffer1 /= buffer
        else:
            if self.func_isfloat(self.buffer_s):
                self.buffer1 = float(self.buffer_s)
            else:
                 self.buffer1 = int(self.buffer_s)
            self.isbuffer = True
        self.ui.lcd.display(self.buffer1)
        self.labeltext.append(self.buffer_s)
        self.labeltext.append(oper)
        labelstr = ''
        for i in self.labeltext:
            labelstr += i + ' '
        self.ui.label.setText(labelstr)
        self.buffer_s = ''
    def func_clear(self):
        self.isbuffer = False
        self.buffer_s = ''
        self.buffer1 = ''
        self.buffer2 = 0
        self.labeltext = []
        self.ui.lcd.display(0)
        self.ui.label.setText('')
    def func_backspace(self):
        self.buffer_s = self.buffer_s[0:-1]
        if float(int(self.buffer_s)) < float(self.buffer_s):  # проверяем, float или int
            self.buffer1 = float(self.buffer_s)
        else:
            self.buffer1 = int(self.buffer_s)
        self.ui.lcd.display(self.buffer_s)
    def func_zpt(self):
        if not self.func_isfloat(self.buffer_s):
            self.buffer_s+='.'
            self.ui.lcd.display(self.buffer_s)
    def func_rev(self):
        if self.buffer_s[0]=='-':
            self.buffer_s = self.buffer_s[1::]
            self.ui.lcd.display(self.buffer_s)
        else:
            self.buffer_s = '-' + self.buffer_s
            self.ui.lcd.display(self.buffer_s)
    def func_percent(self):
        if self.func_isfloat(self.buffer_s):
            buffer = float(self.buffer_s)
        else:
            buffer = int(self.buffer_s)
        self.buffer_s=str(buffer*(self.buffer1/100))
        self.ui.lcd.display(self.buffer_s)

    def func_isfloat(self,number):
        return float(number) if '.' in number else int(number)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperCalc()
    window.show()

    sys.exit(app.exec())
