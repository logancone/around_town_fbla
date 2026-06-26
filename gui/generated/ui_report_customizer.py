# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_customizer.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(439, 413)
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
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.user_info = QCheckBox(Dialog)
        self.user_info.setObjectName(u"user_info")

        self.verticalLayout.addWidget(self.user_info)

        self.bookmarked_businesses = QCheckBox(Dialog)
        self.bookmarked_businesses.setObjectName(u"bookmarked_businesses")

        self.verticalLayout.addWidget(self.bookmarked_businesses)

        self.owned_businesses = QCheckBox(Dialog)
        self.owned_businesses.setObjectName(u"owned_businesses")

        self.verticalLayout.addWidget(self.owned_businesses)

        self.reviews = QCheckBox(Dialog)
        self.reviews.setObjectName(u"reviews")

        self.verticalLayout.addWidget(self.reviews)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Report Details", None))
        self.user_info.setText(QCoreApplication.translate("Dialog", u"User Information", None))
        self.bookmarked_businesses.setText(QCoreApplication.translate("Dialog", u"Bookmarked Businesses", None))
        self.owned_businesses.setText(QCoreApplication.translate("Dialog", u"Owned Businesses", None))
        self.reviews.setText(QCoreApplication.translate("Dialog", u"Review History", None))
    # retranslateUi

