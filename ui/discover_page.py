# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'discover_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(812, 706)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 790, 684))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.discover_label = QLabel(self.scrollAreaWidgetContents_2)
        self.discover_label.setObjectName(u"discover_label")
        self.discover_label.setEnabled(True)
        font = QFont()
        font.setPointSize(25)
        self.discover_label.setFont(font)
        self.discover_label.setTextFormat(Qt.TextFormat.AutoText)
        self.discover_label.setScaledContents(False)
        self.discover_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.discover_label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.discover_label)

        self.search_options = QFrame(self.scrollAreaWidgetContents_2)
        self.search_options.setObjectName(u"search_options")
        self.search_options.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_options.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_options)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_label = QLabel(self.search_options)
        self.filter_label.setObjectName(u"filter_label")
        font1 = QFont()
        font1.setBold(True)
        self.filter_label.setFont(font1)

        self.horizontalLayout.addWidget(self.filter_label)

        self.retail_button = QPushButton(self.search_options)
        self.retail_button.setObjectName(u"retail_button")

        self.horizontalLayout.addWidget(self.retail_button)

        self.food_button = QPushButton(self.search_options)
        self.food_button.setObjectName(u"food_button")

        self.horizontalLayout.addWidget(self.food_button)

        self.entertainment_button = QPushButton(self.search_options)
        self.entertainment_button.setObjectName(u"entertainment_button")

        self.horizontalLayout.addWidget(self.entertainment_button)

        self.services_button = QPushButton(self.search_options)
        self.services_button.setObjectName(u"services_button")

        self.horizontalLayout.addWidget(self.services_button)

        self.sort_label = QLabel(self.search_options)
        self.sort_label.setObjectName(u"sort_label")
        self.sort_label.setFont(font1)

        self.horizontalLayout.addWidget(self.sort_label)

        self.ratings_descending_button = QPushButton(self.search_options)
        self.ratings_descending_button.setObjectName(u"ratings_descending_button")

        self.horizontalLayout.addWidget(self.ratings_descending_button)

        self.ratings_ascending_button = QPushButton(self.search_options)
        self.ratings_ascending_button.setObjectName(u"ratings_ascending_button")

        self.horizontalLayout.addWidget(self.ratings_ascending_button)


        self.verticalLayout_2.addWidget(self.search_options)

        self.business_list = QWidget(self.scrollAreaWidgetContents_2)
        self.business_list.setObjectName(u"business_list")
        self.grid_layout = QGridLayout(self.business_list)
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout_2.addWidget(self.business_list)

        self.verticalLayout_2.setStretch(2, 8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.discover_label.setText(QCoreApplication.translate("Form", u"Discover", None))
        self.filter_label.setText(QCoreApplication.translate("Form", u"Filter By Category:", None))
        self.retail_button.setText(QCoreApplication.translate("Form", u"Retail", None))
        self.food_button.setText(QCoreApplication.translate("Form", u"Food", None))
        self.entertainment_button.setText(QCoreApplication.translate("Form", u"Entertainment", None))
        self.services_button.setText(QCoreApplication.translate("Form", u"Services", None))
        self.sort_label.setText(QCoreApplication.translate("Form", u"Sort By Rating:", None))
        self.ratings_descending_button.setText(QCoreApplication.translate("Form", u"High to Low", None))
        self.ratings_ascending_button.setText(QCoreApplication.translate("Form", u"Low to High", None))
    # retranslateUi

