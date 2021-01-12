# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/pullfile.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PullFile(object):
    def setupUi(self, PullFile):
        PullFile.setObjectName("PullFile")
        PullFile.resize(400, 300)
        PullFile.setStyleSheet("font: 11pt \"Sans Serif\";")
        self.gridLayout = QtWidgets.QGridLayout(PullFile)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(PullFile)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(PullFile)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(PullFile)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(PullFile)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(PullFile)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(PullFile)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(PullFile)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(PullFile)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PullFile)
        QtCore.QMetaObject.connectSlotsByName(PullFile)

    def retranslateUi(self, PullFile):
        _translate = QtCore.QCoreApplication.translate
        PullFile.setWindowTitle(_translate("PullFile", "PullFile"))
        self.label.setText(_translate("PullFile", "点击按钮拉取文件..."))
        self.lineEdit.setText(_translate("PullFile", "/home/user/"))
        self.pushButton_3.setText(_translate("PullFile", "选择路径"))
        self.pushButton.setText(_translate("PullFile", "拉取文件"))
        self.pushButton_2.setText(_translate("PullFile", "取消"))

