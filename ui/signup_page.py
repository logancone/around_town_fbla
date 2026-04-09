# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(612, 589)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalFrame = QFrame(Form)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 172, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.app_title = QLabel(self.verticalFrame)
        self.app_title.setObjectName(u"app_title")
        font = QFont()
        font.setPointSize(35)
        self.app_title.setFont(font)
        self.app_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.app_title)

        self.username_entry = QLineEdit(self.verticalFrame)
        self.username_entry.setObjectName(u"username_entry")

        self.verticalLayout.addWidget(self.username_entry)

        self.password_entry = QLineEdit(self.verticalFrame)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.verticalLayout.addWidget(self.password_entry)

        self.confirm_password_entry = QLineEdit(self.verticalFrame)
        self.confirm_password_entry.setObjectName(u"confirm_password_entry")
        self.confirm_password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.confirm_password_entry)

        self.verticalSpacer_3 = QSpacerItem(10, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.captcha_display = QLabel(self.verticalFrame)
        self.captcha_display.setObjectName(u"captcha_display")

        self.horizontalLayout_2.addWidget(self.captcha_display)

        self.reload_button = QPushButton(self.verticalFrame)
        self.reload_button.setObjectName(u"reload_button")
        self.reload_button.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.reload_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.captcha_entry = QLineEdit(self.verticalFrame)
        self.captcha_entry.setObjectName(u"captcha_entry")

        self.verticalLayout.addWidget(self.captcha_entry)

        self.signup_button = QPushButton(self.verticalFrame)
        self.signup_button.setObjectName(u"signup_button")

        self.verticalLayout.addWidget(self.signup_button)

        self.error_label = QLabel(self.verticalFrame)
        self.error_label.setObjectName(u"error_label")
        font1 = QFont()
        font1.setPointSize(5)
        self.error_label.setFont(font1)

        self.verticalLayout.addWidget(self.error_label)

        self.login_button = QPushButton(self.verticalFrame)
        self.login_button.setObjectName(u"login_button")

        self.verticalLayout.addWidget(self.login_button)

        self.verticalSpacer_2 = QSpacerItem(20, 172, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.app_title.setText(QCoreApplication.translate("Form", u"AroundTown", None))
        self.username_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.confirm_password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.captcha_display.setText("")
        self.reload_button.setText(QCoreApplication.translate("Form", u"\u27f3", None))
        self.captcha_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Type the code seen above", None))
        self.signup_button.setText(QCoreApplication.translate("Form", u"Sign Up!", None))
        self.error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("Form", u"Already have an account? Log in here!", None))
    # retranslateUi

