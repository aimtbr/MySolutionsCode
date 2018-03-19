# -*- coding: utf-8 -*-


#Модуль реализации интерфейса с помощью PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(286, 165)
        self.convert = QtWidgets.QPushButton(Dialog)
        self.convert.setGeometry(QtCore.QRect(90, 70, 111, 23))
        self.convert.setObjectName("convert")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(100, 110, 101, 21))
        self.result.setAutoFillBackground(False)
        self.result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.typein = QtWidgets.QLineEdit(Dialog)
        self.typein.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.typein.setObjectName("typein")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Roman Converter"))
        self.convert.setText(_translate("Dialog", "Convert"))

