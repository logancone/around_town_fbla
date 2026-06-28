# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(660, 588)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.title_label)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 638, 472))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.chat_input = QLineEdit(Form)
        self.chat_input.setObjectName(u"chat_input")

        self.horizontalLayout.addWidget(self.chat_input)

        self.send_button = QPushButton(Form)
        self.send_button.setObjectName(u"send_button")

        self.horizontalLayout.addWidget(self.send_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.warning_label = QLabel(Form)
        self.warning_label.setObjectName(u"warning_label")
        font1 = QFont()
        font1.setPointSize(7)
        self.warning_label.setFont(font1)

        self.verticalLayout_2.addWidget(self.warning_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"AI Assistant", None))
        self.chat_input.setInputMask("")
        self.chat_input.setText(QCoreApplication.translate("Form", u"Give me a business recommendation, explain it, and give me more details about the chosen business.", None))
        self.chat_input.setPlaceholderText(QCoreApplication.translate("Form", u"Type your message here...", None))
        self.send_button.setText(QCoreApplication.translate("Form", u"Send!", None))
        self.warning_label.setText("")
    # retranslateUi

