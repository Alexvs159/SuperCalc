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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 450)
        MainWindow.setMinimumSize(QSize(370, 450))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background: rgb(92, 110, 111);\n"
"	font-family: ;\n"
"	font: 26pt \"Lucida Console\";\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 12pt \"Lucida Console\";\n"
"}")
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_1 = QPushButton(self.main)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Lucida Console"])
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        self.btn_1.setFont(font)

        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)

        self.btn_7 = QPushButton(self.main)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font)

        self.gridLayout.addWidget(self.btn_7, 3, 0, 1, 1)

        self.btn_calc = QPushButton(self.main)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy)
        self.btn_calc.setFont(font)
        self.btn_calc.setAutoFillBackground(False)
        self.btn_calc.setCheckable(False)
        self.btn_calc.setChecked(False)

        self.gridLayout.addWidget(self.btn_calc, 6, 3, 1, 1)

        self.btn_percent = QPushButton(self.main)
        self.btn_percent.setObjectName(u"btn_percent")
        sizePolicy.setHeightForWidth(self.btn_percent.sizePolicy().hasHeightForWidth())
        self.btn_percent.setSizePolicy(sizePolicy)
        self.btn_percent.setFont(font)

        self.gridLayout.addWidget(self.btn_percent, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.main)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)

        self.btn_rev = QPushButton(self.main)
        self.btn_rev.setObjectName(u"btn_rev")
        sizePolicy.setHeightForWidth(self.btn_rev.sizePolicy().hasHeightForWidth())
        self.btn_rev.setSizePolicy(sizePolicy)
        self.btn_rev.setFont(font)

        self.gridLayout.addWidget(self.btn_rev, 6, 0, 1, 1)

        self.btn_minus = QPushButton(self.main)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setFont(font)

        self.gridLayout.addWidget(self.btn_minus, 4, 3, 1, 1)

        self.btn_9 = QPushButton(self.main)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font)

        self.gridLayout.addWidget(self.btn_9, 3, 2, 1, 1)

        self.btn_3 = QPushButton(self.main)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font)

        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)

        self.btn_0 = QPushButton(self.main)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setFont(font)

        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)

        self.btn_zpt = QPushButton(self.main)
        self.btn_zpt.setObjectName(u"btn_zpt")
        sizePolicy.setHeightForWidth(self.btn_zpt.sizePolicy().hasHeightForWidth())
        self.btn_zpt.setSizePolicy(sizePolicy)
        self.btn_zpt.setFont(font)

        self.gridLayout.addWidget(self.btn_zpt, 6, 2, 1, 1)

        self.btn_6 = QPushButton(self.main)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font)

        self.gridLayout.addWidget(self.btn_6, 4, 2, 1, 1)

        self.btn_c = QPushButton(self.main)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        self.btn_c.setFont(font)

        self.gridLayout.addWidget(self.btn_c, 2, 1, 1, 1)

        self.btn_backspace = QPushButton(self.main)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setFont(font)

        self.gridLayout.addWidget(self.btn_backspace, 2, 2, 1, 1)

        self.btn_add = QPushButton(self.main)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setFont(font)

        self.gridLayout.addWidget(self.btn_add, 5, 3, 1, 1)

        self.btn_4 = QPushButton(self.main)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font)

        self.gridLayout.addWidget(self.btn_4, 4, 0, 1, 1)

        self.lcd = QLCDNumber(self.main)
        self.lcd.setObjectName(u"lcd")
        sizePolicy.setHeightForWidth(self.lcd.sizePolicy().hasHeightForWidth())
        self.lcd.setSizePolicy(sizePolicy)
        self.lcd.setFrameShape(QFrame.NoFrame)
        self.lcd.setFrameShadow(QFrame.Plain)
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setDigitCount(20)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout.addWidget(self.lcd, 1, 0, 1, 4)

        self.btn_8 = QPushButton(self.main)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font)

        self.gridLayout.addWidget(self.btn_8, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.main)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font)

        self.gridLayout.addWidget(self.btn_5, 4, 1, 1, 1)

        self.btn_aster = QPushButton(self.main)
        self.btn_aster.setObjectName(u"btn_aster")
        sizePolicy.setHeightForWidth(self.btn_aster.sizePolicy().hasHeightForWidth())
        self.btn_aster.setSizePolicy(sizePolicy)
        self.btn_aster.setFont(font)

        self.gridLayout.addWidget(self.btn_aster, 3, 3, 1, 1)

        self.btn_div = QPushButton(self.main)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setFont(font)

        self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)

        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Lucida Console"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SuperCalc", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.btn_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
#if QT_CONFIG(shortcut)
        self.btn_percent.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_rev.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_zpt.setText(QCoreApplication.translate("MainWindow", u",", None))
#if QT_CONFIG(shortcut)
        self.btn_zpt.setShortcut(QCoreApplication.translate("MainWindow", u",", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.btn_c.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"<--", None))
#if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_aster.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_aster.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText("")
    # retranslateUi

