# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'location_editor.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.latitude_input = QLineEdit(Dialog)
        self.latitude_input.setObjectName(u"latitude_input")

        self.gridLayout.addWidget(self.latitude_input, 0, 1, 1, 1)

        self.longitude_input = QLineEdit(Dialog)
        self.longitude_input.setObjectName(u"longitude_input")

        self.gridLayout.addWidget(self.longitude_input, 1, 1, 1, 1)

        self.latitude_label = QLabel(Dialog)
        self.latitude_label.setObjectName(u"latitude_label")

        self.gridLayout.addWidget(self.latitude_label, 0, 0, 1, 1)

        self.longitude_label = QLabel(Dialog)
        self.longitude_label.setObjectName(u"longitude_label")

        self.gridLayout.addWidget(self.longitude_label, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.error_label = QLabel(Dialog)
        self.error_label.setObjectName(u"error_label")
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(7)
        self.error_label.setFont(font1)

        self.verticalLayout.addWidget(self.error_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.restore_defaults_button = QPushButton(Dialog)
        self.restore_defaults_button.setObjectName(u"restore_defaults_button")

        self.horizontalLayout.addWidget(self.restore_defaults_button)

        self.ok_button = QPushButton(Dialog)
        self.ok_button.setObjectName(u"ok_button")

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Please Enter Your Location", None))
#if QT_CONFIG(accessibility)
        self.latitude_input.setAccessibleName(QCoreApplication.translate("Dialog", u"Latitude Text Entry", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.latitude_input.setAccessibleDescription(QCoreApplication.translate("Dialog", u"Please enter your current latitude coordinate.", None))
#endif // QT_CONFIG(accessibility)
        self.latitude_input.setText("")
        self.latitude_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please enter current latitude...", None))
#if QT_CONFIG(accessibility)
        self.longitude_input.setAccessibleName(QCoreApplication.translate("Dialog", u"Longitude Text Entry", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.longitude_input.setAccessibleDescription(QCoreApplication.translate("Dialog", u"Please enter your current longitude coordinate.", None))
#endif // QT_CONFIG(accessibility)
        self.longitude_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please enter current longitude...", None))
        self.latitude_label.setText(QCoreApplication.translate("Dialog", u"Latitude:", None))
        self.longitude_label.setText(QCoreApplication.translate("Dialog", u"Longitude:", None))
        self.error_label.setText("")
        self.restore_defaults_button.setText(QCoreApplication.translate("Dialog", u"Restore Defaults", None))
        self.ok_button.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

