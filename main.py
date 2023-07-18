import sys

from window import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

class SuperCalc(QMainWindow):
    def __init__(self):
        super(SuperCalc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def testfunc(self):
        self.ui.edit.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SuperCalc()
    window.show()

    sys.exit(app.exec())