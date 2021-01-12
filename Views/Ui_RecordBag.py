# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/recordbag.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RecordBag(object):
    def setupUi(self, RecordBag):
        RecordBag.setObjectName("RecordBag")
        RecordBag.resize(400, 297)
        RecordBag.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(RecordBag)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(RecordBag)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(RecordBag)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(RecordBag)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(RecordBag)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(RecordBag)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RecordBag)
        QtCore.QMetaObject.connectSlotsByName(RecordBag)

    def retranslateUi(self, RecordBag):
        _translate = QtCore.QCoreApplication.translate
        RecordBag.setWindowTitle(_translate("RecordBag", "RecordBag"))
        self.label.setText(_translate("RecordBag", "输入板子ip地址:"))
        self.pushButton.setText(_translate("RecordBag", "记录bag包"))
        self.pushButton_2.setText(_translate("RecordBag", "取消"))

