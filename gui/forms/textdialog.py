# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/textdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TextDialog(object):
    def setupUi(self, TextDialog):
        TextDialog.setObjectName("TextDialog")
        TextDialog.resize(517, 653)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextDialog)
        self.verticalLayout.setContentsMargins(3, 5, 3, 5)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(TextDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.designLbl = QtWidgets.QLineEdit(TextDialog)
        self.designLbl.setFocusPolicy(QtCore.Qt.NoFocus)
        self.designLbl.setReadOnly(True)
        self.designLbl.setObjectName("designLbl")
        self.horizontalLayout_3.addWidget(self.designLbl)
        self.designBtn = QtWidgets.QToolButton(TextDialog)
        self.designBtn.setObjectName("designBtn")
        self.horizontalLayout_3.addWidget(self.designBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.searchOptionLayout = QtWidgets.QHBoxLayout()
        self.searchOptionLayout.setSpacing(0)
        self.searchOptionLayout.setObjectName("searchOptionLayout")
        self.label_3 = QtWidgets.QLabel(TextDialog)
        self.label_3.setObjectName("label_3")
        self.searchOptionLayout.addWidget(self.label_3)
        self.followEdit = QtWidgets.QLineEdit(TextDialog)
        self.followEdit.setText("")
        self.followEdit.setObjectName("followEdit")
        self.searchOptionLayout.addWidget(self.followEdit)
        self.verticalLayout.addLayout(self.searchOptionLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dlAllBtn = QtWidgets.QPushButton(TextDialog)
        self.dlAllBtn.setAutoDefault(False)
        self.dlAllBtn.setObjectName("dlAllBtn")
        self.horizontalLayout_5.addWidget(self.dlAllBtn)
        self.stopBtn = QtWidgets.QPushButton(TextDialog)
        self.stopBtn.setEnabled(True)
        self.stopBtn.setAutoDefault(False)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_5.addWidget(self.stopBtn)
        self.clearAllBtn = QtWidgets.QPushButton(TextDialog)
        self.clearAllBtn.setAutoDefault(False)
        self.clearAllBtn.setObjectName("clearAllBtn")
        self.horizontalLayout_5.addWidget(self.clearAllBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.imgList = QtWidgets.QListWidget(TextDialog)
        self.imgList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imgList.setAutoScroll(False)
        self.imgList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.imgList.setObjectName("imgList")
        self.verticalLayout.addWidget(self.imgList)
        self.line = QtWidgets.QFrame(TextDialog)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(7)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelBtn = QtWidgets.QPushButton(TextDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.startBtn = QtWidgets.QPushButton(TextDialog)
        self.startBtn.setAutoDefault(False)
        self.startBtn.setDefault(False)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(TextDialog)
        QtCore.QMetaObject.connectSlotsByName(TextDialog)

    def retranslateUi(self, TextDialog):
        _translate = QtCore.QCoreApplication.translate
        TextDialog.setWindowTitle(_translate("TextDialog", "Text Setting"))
        self.label_2.setText(_translate("TextDialog", "Book Design: "))
        self.designBtn.setText(_translate("TextDialog", "..."))
        self.label_3.setText(_translate("TextDialog", "Extra Search Keyword: "))
        self.followEdit.setPlaceholderText(_translate("TextDialog", "Input text to add search keywords"))
        self.dlAllBtn.setText(_translate("TextDialog", "Download All Images"))
        self.stopBtn.setText(_translate("TextDialog", "Stop Download"))
        self.clearAllBtn.setText(_translate("TextDialog", "Clear All"))
        self.cancelBtn.setText(_translate("TextDialog", "Stop"))
        self.startBtn.setText(_translate("TextDialog", "Create Textbook"))

