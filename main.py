import sys
from window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class SuperCalc(QMainWindow):

    def __init__(self):
        super(SuperCalc, self).__init__()
        self.display = ''
        self.numbers = []
        self.labeltext = []
        self.last_operation = None
        self.last_value = None
        self.isPercentInput = False
        self.isDigitInput = False
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
        if len(self.display) < 20:
            self.display += str(number)
            self.ui.lcd.display(self.display)
            self.isDigitInput = True

    # Функция кнопок операций +-*/
    def func_btn_oper(self, oper):
        self.last_operation = oper
        if self.isDigitInput:
            self.numbers.append(self.func_isfloat(self.display))
            self.display = ''
            self.isDigitInput = False
            if len(self.numbers) > 1:
                result = self.func_oper(oper, self.numbers[-2], self.numbers[-1])
                self.numbers = [result]
                self.display = str(self.numbers[-1])
                self.ui.lcd.display(self.display)
                self.display = ''

    def func_equal(self):
        if self.isDigitInput:
            if self.isPercentInput is False:
                self.numbers.append(self.func_isfloat(self.display))
            else:
                self.isPercentInput = False
            result = self.func_oper(self.last_operation, self.numbers[-2], self.numbers[-1])
            self.display = str(result)
            self.ui.lcd.display(self.display)
            self.last_value = self.numbers[-1]
            self.display = ''
            self.numbers = [result]
            self.isDigitInput = False
        elif self.last_value is not None:
            result = self.func_oper(self.last_operation, self.last_value, self.numbers[-1])
            self.numbers = [result]
            self.display = str(result)
            self.ui.lcd.display(self.display)
            self.display = ''

    def func_oper(self, oper, num1, num2):
        if oper == '+':
            return num1 + num2
        if oper == '-':
            return num1 - num2
        if oper == '*':
            return num1 * num2
        if oper == '/':
            return num1 / num2

    def func_clear(self):
        self.display = ''
        self.ui.lcd.display('0')
        self.numbers = []
        self.last_value = None
        self.isDigitInput = False
        self.isPercentInput = False

    def func_backspace(self):
        self.display = self.display[0:-1]
        self.ui.lcd.display(self.display)

    def func_zpt(self):
        if '.' not in self.display and len(self.display) < 20:
            self.display += '.'
            self.ui.lcd.display(self.display)

    def func_rev(self):  # изменение знака
        if self.display[0] == '-':
            self.display = self.display[1::]
            self.ui.lcd.display(self.display)
        else:
            self.display = '-' + self.display
            self.ui.lcd.display(self.display)

    def func_percent(self):
        if len(self.numbers) > 0:
            percent = self.numbers[-1] / 100 * self.func_isfloat(self.display)
            self.numbers.append(percent)
            self.isPercentInput = True
            self.display = str(percent)
            self.ui.lcd.display(self.display)
            self.display = ''

    def func_isfloat(self, number):  # Определение типа числа
        if '.' in number:
            return float(number)
        else:
            return int(number)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperCalc()
    window.show()

    sys.exit(app.exec())
