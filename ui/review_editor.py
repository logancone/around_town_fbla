# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'review_editor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPlainTextEdit, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(522, 408)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rating_bar = QSlider(self.widget)
        self.rating_bar.setObjectName(u"rating_bar")
        self.rating_bar.setMaximum(50)
        self.rating_bar.setSingleStep(5)
        self.rating_bar.setOrientation(Qt.Orientation.Horizontal)
        self.rating_bar.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.rating_bar.setTickInterval(10)

        self.horizontalLayout.addWidget(self.rating_bar)

        self.rating_label = QLabel(self.widget)
        self.rating_label.setObjectName(u"rating_label")

        self.horizontalLayout.addWidget(self.rating_label)


        self.verticalLayout.addWidget(self.widget)

        self.review_content = QPlainTextEdit(Dialog)
        self.review_content.setObjectName(u"review_content")

        self.verticalLayout.addWidget(self.review_content)

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
        self.rating_label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.review_content.setPlainText("")
        self.review_content.setPlaceholderText(QCoreApplication.translate("Dialog", u"Type Review Here...", None))
    # retranslateUi

