# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(465, 397)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.edit = QLineEdit(self.main)
        self.edit.setObjectName(u"edit")
        self.edit.setGeometry(QRect(10, 10, 301, 41))
        font = QFont()
        font.setFamilies([u"Arial Narrow"])
        font.setPointSize(12)
        self.edit.setFont(font)
        self.edit.setReadOnly(True)
        self.add = QPushButton(self.main)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(20, 90, 75, 24))
        self.button_1 = QPushButton(self.main)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(20, 140, 75, 24))
        self.calc = QPushButton(self.main)
        self.calc.setObjectName(u"calc")
        self.calc.setGeometry(QRect(120, 140, 75, 24))
        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

