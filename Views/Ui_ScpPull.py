# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/scppull.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScpPull(object):
    def setupUi(self, ScpPull):
        ScpPull.setObjectName("ScpPull")
        ScpPull.resize(401, 297)
        ScpPull.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(ScpPull)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(ScpPull)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(ScpPull)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(ScpPull)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(ScpPull)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(ScpPull)
        self.label_2.setStyleSheet("LOG保存路径")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(ScpPull)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(ScpPull)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(ScpPull)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ScpPull)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(ScpPull)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(ScpPull)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ScpPull)
        QtCore.QMetaObject.connectSlotsByName(ScpPull)

    def retranslateUi(self, ScpPull):
        _translate = QtCore.QCoreApplication.translate
        ScpPull.setWindowTitle(_translate("ScpPull", "ScpPull"))
        self.label_5.setText(_translate("ScpPull", "请输入板子IP:"))
        self.label.setText(_translate("ScpPull", "拉取文件路径:"))
        self.label_2.setText(_translate("ScpPull", "保存文件路径:"))
        self.pushButton_3.setText(_translate("ScpPull", "选择路径"))
        self.pushButton.setText(_translate("ScpPull", "拉取文件"))
        self.pushButton_2.setText(_translate("ScpPull", "取消拉取"))

