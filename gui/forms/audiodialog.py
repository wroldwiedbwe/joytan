# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/audiodialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AudioDialog(object):
    def setupUi(self, AudioDialog):
        AudioDialog.setObjectName("AudioDialog")
        AudioDialog.resize(507, 653)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AudioDialog)
        self.verticalLayout_2.setContentsMargins(9, -1, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(AudioDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.settingBtn = QtWidgets.QPushButton(AudioDialog)
        self.settingBtn.setObjectName("settingBtn")
        self.horizontalLayout_2.addWidget(self.settingBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lrcCheck = QtWidgets.QCheckBox(AudioDialog)
        self.lrcCheck.setChecked(True)
        self.lrcCheck.setObjectName("lrcCheck")
        self.horizontalLayout_6.addWidget(self.lrcCheck)
        self.idxCheck = QtWidgets.QCheckBox(AudioDialog)
        self.idxCheck.setChecked(True)
        self.idxCheck.setObjectName("idxCheck")
        self.horizontalLayout_6.addWidget(self.idxCheck)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(AudioDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.flowAdd = QtWidgets.QToolButton(AudioDialog)
        self.flowAdd.setObjectName("flowAdd")
        self.horizontalLayout_7.addWidget(self.flowAdd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.flowList = QtWidgets.QListWidget(AudioDialog)
        self.flowList.setStyleSheet("QListWidget::item { background: rgb(180, 180, 180); }")
        self.flowList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.flowList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.flowList.setObjectName("flowList")
        self.verticalLayout_3.addWidget(self.flowList)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(AudioDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.bgmAdd = QtWidgets.QToolButton(AudioDialog)
        self.bgmAdd.setObjectName("bgmAdd")
        self.horizontalLayout_8.addWidget(self.bgmAdd)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.bgmList = QtWidgets.QListWidget(AudioDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgmList.sizePolicy().hasHeightForWidth())
        self.bgmList.setSizePolicy(sizePolicy)
        self.bgmList.setStyleSheet("QListWidget::item { background: rgb(150, 150, 150); }")
        self.bgmList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.bgmList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.bgmList.setObjectName("bgmList")
        self.verticalLayout_3.addWidget(self.bgmList)
        self.line = QtWidgets.QFrame(AudioDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(AudioDialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.pgMsg = QtWidgets.QLabel(AudioDialog)
        self.pgMsg.setText("")
        self.pgMsg.setObjectName("pgMsg")
        self.horizontalLayout.addWidget(self.pgMsg)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(AudioDialog)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.stopBtn = QtWidgets.QPushButton(AudioDialog)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout_5.addWidget(self.stopBtn)
        self.createBtn = QtWidgets.QPushButton(AudioDialog)
        self.createBtn.setCheckable(False)
        self.createBtn.setAutoDefault(False)
        self.createBtn.setDefault(True)
        self.createBtn.setObjectName("createBtn")
        self.horizontalLayout_5.addWidget(self.createBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(AudioDialog)
        QtCore.QMetaObject.connectSlotsByName(AudioDialog)

    def retranslateUi(self, AudioDialog):
        _translate = QtCore.QCoreApplication.translate
        AudioDialog.setWindowTitle(_translate("AudioDialog", "Audio Setting"))
        self.label.setText(_translate("AudioDialog", "Text-to-Speech Service:"))
        self.settingBtn.setText(_translate("AudioDialog", "Setting"))
        self.lrcCheck.setText(_translate("AudioDialog", "Create Lyrics file"))
        self.idxCheck.setText(_translate("AudioDialog", "Read index"))
        self.label_2.setText(_translate("AudioDialog", "<html><head/><body><p>Audio Flow</p></body></html>"))
        self.flowAdd.setText(_translate("AudioDialog", "Add Item"))
        self.label_3.setText(_translate("AudioDialog", "BGM Loop"))
        self.bgmAdd.setText(_translate("AudioDialog", "Add Item"))
        self.label_7.setText(_translate("AudioDialog", "Progress:"))
        self.stopBtn.setText(_translate("AudioDialog", "Stop"))
        self.createBtn.setText(_translate("AudioDialog", "Start"))

