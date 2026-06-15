# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'business_card.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 135)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(250, 135))
        Form.setMaximumSize(QSize(250, 135))
        Form.setFrameShape(QFrame.Shape.Box)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setWordWrap(True)

        self.verticalLayout.addWidget(self.title)

        self.category = QLabel(Form)
        self.category.setObjectName(u"category")
        font1 = QFont()
        font1.setPointSize(11)
        self.category.setFont(font1)

        self.verticalLayout.addWidget(self.category)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.ratings = QLabel(Form)
        self.ratings.setObjectName(u"ratings")
        self.ratings.setFont(font1)

        self.horizontalLayout_3.addWidget(self.ratings)

        self.bookmark_button = QPushButton(Form)
        self.bookmark_button.setObjectName(u"bookmark_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bookmark_button.sizePolicy().hasHeightForWidth())
        self.bookmark_button.setSizePolicy(sizePolicy1)
        self.bookmark_button.setMaximumSize(QSize(27, 27))
        self.bookmark_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.bookmark_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.thumbnail = QLabel(Form)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setScaledContents(True)

        self.horizontalLayout.addWidget(self.thumbnail)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.category.setText(QCoreApplication.translate("Form", u"Category", None))
        self.ratings.setText(QCoreApplication.translate("Form", u"\u2b505.0 (100)", None))
        self.bookmark_button.setText("")
        self.thumbnail.setText("")
    # retranslateUi

