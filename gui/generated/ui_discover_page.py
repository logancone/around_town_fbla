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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 706)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 758, 684))
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

        self.search_bar = QLineEdit(self.scrollAreaWidgetContents_2)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setMinimumSize(QSize(0, 35))
        self.search_bar.setEchoMode(QLineEdit.EchoMode.Normal)

        self.verticalLayout_2.addWidget(self.search_bar)

        self.search_options = QFrame(self.scrollAreaWidgetContents_2)
        self.search_options.setObjectName(u"search_options")
        self.search_options.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_options.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_options)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sort_label = QLabel(self.search_options)
        self.sort_label.setObjectName(u"sort_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sort_label.sizePolicy().hasHeightForWidth())
        self.sort_label.setSizePolicy(sizePolicy1)
        self.sort_label.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.sort_label.setFont(font1)

        self.horizontalLayout.addWidget(self.sort_label)

        self.sort_dropdown = QComboBox(self.search_options)
        self.sort_dropdown.addItem("")
        self.sort_dropdown.addItem("")
        self.sort_dropdown.addItem("")
        self.sort_dropdown.addItem("")
        self.sort_dropdown.setObjectName(u"sort_dropdown")
        self.sort_dropdown.setEditable(False)

        self.horizontalLayout.addWidget(self.sort_dropdown)

        self.filter_label = QLabel(self.search_options)
        self.filter_label.setObjectName(u"filter_label")
        sizePolicy1.setHeightForWidth(self.filter_label.sizePolicy().hasHeightForWidth())
        self.filter_label.setSizePolicy(sizePolicy1)
        self.filter_label.setMaximumSize(QSize(16777215, 16777215))
        self.filter_label.setFont(font1)

        self.horizontalLayout.addWidget(self.filter_label)

        self.category_dropdown = QComboBox(self.search_options)
        self.category_dropdown.addItem("")
        self.category_dropdown.addItem("")
        self.category_dropdown.addItem("")
        self.category_dropdown.addItem("")
        self.category_dropdown.addItem("")
        self.category_dropdown.setObjectName(u"category_dropdown")

        self.horizontalLayout.addWidget(self.category_dropdown)

        self.distance_dropdown = QComboBox(self.search_options)
        self.distance_dropdown.addItem("")
        self.distance_dropdown.addItem("")
        self.distance_dropdown.addItem("")
        self.distance_dropdown.addItem("")
        self.distance_dropdown.addItem("")
        self.distance_dropdown.setObjectName(u"distance_dropdown")

        self.horizontalLayout.addWidget(self.distance_dropdown)

        self.reset_button = QPushButton(self.search_options)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout.addWidget(self.reset_button)


        self.verticalLayout_2.addWidget(self.search_options)

        self.business_list = QWidget(self.scrollAreaWidgetContents_2)
        self.business_list.setObjectName(u"business_list")
        self.grid_layout = QGridLayout(self.business_list)
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout_2.addWidget(self.business_list)

        self.verticalLayout_2.setStretch(3, 8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.discover_label.setText(QCoreApplication.translate("Form", u"Discover", None))
        self.search_bar.setInputMask("")
        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("Form", u"Type here to search...", None))
        self.sort_label.setText(QCoreApplication.translate("Form", u"Sort:", None))
        self.sort_dropdown.setItemText(0, QCoreApplication.translate("Form", u"Recommended", None))
        self.sort_dropdown.setItemText(1, QCoreApplication.translate("Form", u"Rating (High to Low)", None))
        self.sort_dropdown.setItemText(2, QCoreApplication.translate("Form", u"Rating (Low to High)", None))
        self.sort_dropdown.setItemText(3, QCoreApplication.translate("Form", u"Distance", None))

#if QT_CONFIG(accessibility)
        self.sort_dropdown.setAccessibleName(QCoreApplication.translate("Form", u"Sort Dropdown Menu", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.sort_dropdown.setAccessibleDescription(QCoreApplication.translate("Form", u"Open to choose a parameter to sort businesses by", None))
#endif // QT_CONFIG(accessibility)
        self.sort_dropdown.setCurrentText(QCoreApplication.translate("Form", u"Recommended", None))
        self.filter_label.setText(QCoreApplication.translate("Form", u"Filter:", None))
        self.category_dropdown.setItemText(0, QCoreApplication.translate("Form", u"All Categories", None))
        self.category_dropdown.setItemText(1, QCoreApplication.translate("Form", u"Retail", None))
        self.category_dropdown.setItemText(2, QCoreApplication.translate("Form", u"Food", None))
        self.category_dropdown.setItemText(3, QCoreApplication.translate("Form", u"Entertainment", None))
        self.category_dropdown.setItemText(4, QCoreApplication.translate("Form", u"Services", None))

#if QT_CONFIG(accessibility)
        self.category_dropdown.setAccessibleName(QCoreApplication.translate("Form", u"Category Filter Dropdown Menu", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.category_dropdown.setAccessibleDescription(QCoreApplication.translate("Form", u"Open to select a category filter", None))
#endif // QT_CONFIG(accessibility)
        self.distance_dropdown.setItemText(0, QCoreApplication.translate("Form", u"Any Distance", None))
        self.distance_dropdown.setItemText(1, QCoreApplication.translate("Form", u"Within 5 Miles", None))
        self.distance_dropdown.setItemText(2, QCoreApplication.translate("Form", u"Within 10 Miles", None))
        self.distance_dropdown.setItemText(3, QCoreApplication.translate("Form", u"Within 25 Miles", None))
        self.distance_dropdown.setItemText(4, QCoreApplication.translate("Form", u"Within 50 Miles", None))

#if QT_CONFIG(accessibility)
        self.distance_dropdown.setAccessibleName(QCoreApplication.translate("Form", u"Distance Filter Dropdown Menu", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.distance_dropdown.setAccessibleDescription(QCoreApplication.translate("Form", u"Open to select a distance to filter by", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.reset_button.setToolTip(QCoreApplication.translate("Form", u"Resets all discover parameters", None))
#endif // QT_CONFIG(tooltip)
        self.reset_button.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

