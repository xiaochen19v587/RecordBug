# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/openrviz.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenRviz(object):
    def setupUi(self, OpenRviz):
        OpenRviz.setObjectName("OpenRviz")
        OpenRviz.resize(400, 297)
        OpenRviz.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(OpenRviz)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(OpenRviz)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(OpenRviz)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_2 = QtWidgets.QLabel(OpenRviz)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(OpenRviz)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(OpenRviz)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(OpenRviz)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(OpenRviz)
        QtCore.QMetaObject.connectSlotsByName(OpenRviz)

    def retranslateUi(self, OpenRviz):
        _translate = QtCore.QCoreApplication.translate
        OpenRviz.setWindowTitle(_translate("OpenRviz", "OpenRviz"))
        self.label.setText(_translate("OpenRviz", "输入板子ip地址:"))
        self.pushButton.setText(_translate("OpenRviz", "打开rviz"))
        self.pushButton_3.setText(_translate("OpenRviz", "记录bag包"))
        self.pushButton_2.setText(_translate("OpenRviz", "取消"))

