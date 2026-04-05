# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nav_shell.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(664, 579)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navbar = QFrame(Form)
        self.navbar.setObjectName(u"navbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy1)
        self.navbar.setFrameShape(QFrame.Shape.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.navbar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.profile_button = QPushButton(self.navbar)
        self.profile_button.setObjectName(u"profile_button")

        self.verticalLayout_3.addWidget(self.profile_button)

        self.discover_button = QPushButton(self.navbar)
        self.discover_button.setObjectName(u"discover_button")

        self.verticalLayout_3.addWidget(self.discover_button)

        self.logout_button = QPushButton(self.navbar)
        self.logout_button.setObjectName(u"logout_button")

        self.verticalLayout_3.addWidget(self.logout_button)


        self.horizontalLayout.addWidget(self.navbar)

        self.page_stack = QStackedWidget(Form)
        self.page_stack.setObjectName(u"page_stack")
        sizePolicy.setHeightForWidth(self.page_stack.sizePolicy().hasHeightForWidth())
        self.page_stack.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page_stack.addWidget(self.page)

        self.horizontalLayout.addWidget(self.page_stack)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.profile_button.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.discover_button.setText(QCoreApplication.translate("Form", u"Discover", None))
        self.logout_button.setText(QCoreApplication.translate("Form", u"Log Out", None))
    # retranslateUi

