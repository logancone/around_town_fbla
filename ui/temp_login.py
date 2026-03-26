# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temp_login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 180, 112, 114))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.login_label = QLabel(self.widget)
        self.login_label.setObjectName(u"login_label")

        self.verticalLayout_2.addWidget(self.login_label)

        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setEchoMode(QLineEdit.EchoMode.Normal)

        self.verticalLayout_2.addWidget(self.username_input)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setFrame(True)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.password_input)

        self.login_button = QPushButton(self.widget)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout_2.addWidget(self.login_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username_input.setInputMask("")
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.password_input.setInputMask("")
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

