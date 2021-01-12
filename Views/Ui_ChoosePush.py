# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/choosepush.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChoosePush(object):
    def setupUi(self, ChoosePush):
        ChoosePush.setObjectName("ChoosePush")
        ChoosePush.resize(400, 300)
        ChoosePush.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(ChoosePush)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(ChoosePush)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(ChoosePush)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.radioButton = QtWidgets.QRadioButton(ChoosePush)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.label_4 = QtWidgets.QLabel(ChoosePush)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.radioButton_2 = QtWidgets.QRadioButton(ChoosePush)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(ChoosePush)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(ChoosePush)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(ChoosePush)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(ChoosePush)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ChoosePush)
        QtCore.QMetaObject.connectSlotsByName(ChoosePush)

    def retranslateUi(self, ChoosePush):
        _translate = QtCore.QCoreApplication.translate
        ChoosePush.setWindowTitle(_translate("ChoosePush", "ChoosePush"))
        self.label_2.setText(_translate("ChoosePush", "选择推送文件的方式:"))
        self.radioButton.setText(_translate("ChoosePush", "通过adb方式推送文件"))
        self.radioButton_2.setText(_translate("ChoosePush", "通过scp方式推送文件"))
        self.pushButton.setText(_translate("ChoosePush", "确定"))
        self.pushButton_2.setText(_translate("ChoosePush", "取消"))

