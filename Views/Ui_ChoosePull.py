# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/choosepull.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoosePull(object):
    def setupUi(self, ChoosePull):
        ChoosePull.setObjectName("ChoosePull")
        ChoosePull.resize(400, 300)
        ChoosePull.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(ChoosePull)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(ChoosePull)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(ChoosePull)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(ChoosePull)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.label_4 = QtWidgets.QLabel(ChoosePull)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.radioButton_2 = QtWidgets.QRadioButton(ChoosePull)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(ChoosePull)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(ChoosePull)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(ChoosePull)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(ChoosePull)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ChoosePull)
        QtCore.QMetaObject.connectSlotsByName(ChoosePull)

    def retranslateUi(self, ChoosePull):
        _translate = QtCore.QCoreApplication.translate
        ChoosePull.setWindowTitle(_translate("ChoosePull", "ChoosePull"))
        self.label_2.setText(_translate("ChoosePull", "选择拉取文件的方式:"))
        self.radioButton.setText(_translate("ChoosePull", "通过adb方式拉取文件"))
        self.radioButton_2.setText(_translate("ChoosePull", "通过scp方式拉取文件"))
        self.pushButton.setText(_translate("ChoosePull", "确定"))
        self.pushButton_2.setText(_translate("ChoosePull", "取消"))

