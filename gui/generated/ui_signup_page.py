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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.captcha_display = QLabel(self.verticalFrame)
        self.captcha_display.setObjectName(u"captcha_display")
        self.captcha_display.setMinimumSize(QSize(200, 50))
        self.captcha_display.setMaximumSize(QSize(200, 50))

        self.verticalLayout_2.addWidget(self.captcha_display)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.audio_captcha_label = QLabel(self.verticalFrame)
        self.audio_captcha_label.setObjectName(u"audio_captcha_label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.audio_captcha_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.audio_captcha_label)

        self.audio_play_button = QPushButton(self.verticalFrame)
        self.audio_play_button.setObjectName(u"audio_play_button")
        self.audio_play_button.setMinimumSize(QSize(30, 30))
        self.audio_play_button.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.audio_play_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.reload_button = QPushButton(self.verticalFrame)
        self.reload_button.setObjectName(u"reload_button")
        self.reload_button.setMaximumSize(QSize(30, 30))
        font2 = QFont()
        font2.setBold(True)
        self.reload_button.setFont(font2)

        self.horizontalLayout_3.addWidget(self.reload_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.captcha_entry = QLineEdit(self.verticalFrame)
        self.captcha_entry.setObjectName(u"captcha_entry")

        self.verticalLayout.addWidget(self.captcha_entry)

        self.signup_button = QPushButton(self.verticalFrame)
        self.signup_button.setObjectName(u"signup_button")

        self.verticalLayout.addWidget(self.signup_button)

        self.error_label = QLabel(self.verticalFrame)
        self.error_label.setObjectName(u"error_label")
        font3 = QFont()
        font3.setPointSize(5)
        self.error_label.setFont(font3)

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
#if QT_CONFIG(accessibility)
        self.username_entry.setAccessibleName(QCoreApplication.translate("Form", u"Username", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.username_entry.setAccessibleDescription(QCoreApplication.translate("Form", u"Enter your new username", None))
#endif // QT_CONFIG(accessibility)
        self.username_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
#if QT_CONFIG(accessibility)
        self.password_entry.setAccessibleName(QCoreApplication.translate("Form", u"Password", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.password_entry.setAccessibleDescription(QCoreApplication.translate("Form", u"Enter your new password", None))
#endif // QT_CONFIG(accessibility)
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
#if QT_CONFIG(accessibility)
        self.confirm_password_entry.setAccessibleName(QCoreApplication.translate("Form", u"Password", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.confirm_password_entry.setAccessibleDescription(QCoreApplication.translate("Form", u"Enter your new password again", None))
#endif // QT_CONFIG(accessibility)
        self.confirm_password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.captcha_display.setText("")
        self.audio_captcha_label.setText(QCoreApplication.translate("Form", u"Play Audio CAPTCHA", None))
#if QT_CONFIG(accessibility)
        self.audio_play_button.setAccessibleName(QCoreApplication.translate("Form", u"Audio CAPTCHA Play Button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.audio_play_button.setAccessibleDescription(QCoreApplication.translate("Form", u"Plays the CAPTCHA aloud", None))
#endif // QT_CONFIG(accessibility)
        self.audio_play_button.setText("")
#if QT_CONFIG(tooltip)
        self.reload_button.setToolTip(QCoreApplication.translate("Form", u"Load a new CAPTCHA", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.reload_button.setAccessibleDescription(QCoreApplication.translate("Form", u"CAPTCHA Reload Button", None))
#endif // QT_CONFIG(accessibility)
        self.reload_button.setAccessibleIdentifier(QCoreApplication.translate("Form", u"Refresh the captcha to choose a new one", None))
        self.reload_button.setText(QCoreApplication.translate("Form", u"\u27f3", None))
#if QT_CONFIG(accessibility)
        self.captcha_entry.setAccessibleName(QCoreApplication.translate("Form", u"CAPTCHA entry", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.captcha_entry.setAccessibleDescription(QCoreApplication.translate("Form", u"Enter the CAPTCHA answer", None))
#endif // QT_CONFIG(accessibility)
        self.captcha_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Type the code seen/heard above", None))
        self.signup_button.setText(QCoreApplication.translate("Form", u"Sign Up!", None))
        self.error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("Form", u"Already have an account? Log in here!", None))
    # retranslateUi

