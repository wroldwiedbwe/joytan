# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(508, 405)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Preferences)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(Preferences)
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setToolTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tabGeneral = QtWidgets.QWidget()
        self.tabGeneral.setObjectName("tabGeneral")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabGeneral)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tabGeneral)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.titleEdit = QtWidgets.QLineEdit(self.tabGeneral)
        self.titleEdit.setObjectName("titleEdit")
        self.horizontalLayout_6.addWidget(self.titleEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.tabGeneral)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.sourceCombo = QtWidgets.QComboBox(self.tabGeneral)
        self.sourceCombo.setObjectName("sourceCombo")
        self.sourceCombo.addItem("")
        self.sourceCombo.addItem("")
        self.sourceCombo.addItem("")
        self.sourceCombo.addItem("")
        self.horizontalLayout_5.addWidget(self.sourceCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tabGeneral)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.dpwSpin = QtWidgets.QSpinBox(self.tabGeneral)
        self.dpwSpin.setMinimum(1)
        self.dpwSpin.setMaximum(9)
        self.dpwSpin.setProperty("value", 1)
        self.dpwSpin.setObjectName("dpwSpin")
        self.horizontalLayout_3.addWidget(self.dpwSpin)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tabGeneral)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.epdSpin = QtWidgets.QSpinBox(self.tabGeneral)
        self.epdSpin.setMinimum(1)
        self.epdSpin.setMaximum(9)
        self.epdSpin.setObjectName("epdSpin")
        self.horizontalLayout_4.addWidget(self.epdSpin)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.tabGeneral)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sfxEdit = QtWidgets.QLineEdit(self.tabGeneral)
        self.sfxEdit.setObjectName("sfxEdit")
        self.gridLayout.addWidget(self.sfxEdit, 2, 1, 1, 1)
        self.bgmEdit = QtWidgets.QLineEdit(self.tabGeneral)
        self.bgmEdit.setObjectName("bgmEdit")
        self.gridLayout.addWidget(self.bgmEdit, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tabGeneral)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.workingEdit = QtWidgets.QLineEdit(self.tabGeneral)
        self.workingEdit.setObjectName("workingEdit")
        self.gridLayout.addWidget(self.workingEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tabGeneral)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.wordEdit = QtWidgets.QLineEdit(self.tabGeneral)
        self.wordEdit.setObjectName("wordEdit")
        self.gridLayout.addWidget(self.wordEdit, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tabGeneral)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tabGeneral)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabTTS = QtWidgets.QWidget()
        self.tabTTS.setObjectName("tabTTS")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabTTS)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.tabTTS)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.ttsCombo = QtWidgets.QComboBox(self.tabTTS)
        self.ttsCombo.setObjectName("ttsCombo")
        self.horizontalLayout.addWidget(self.ttsCombo)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.label_10 = QtWidgets.QLabel(self.tabTTS)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.testList = QtWidgets.QListWidget(self.tabTTS)
        self.testList.setObjectName("testList")
        self.verticalLayout_6.addWidget(self.testList)
        self.tabWidget.addTab(self.tabTTS, "")
        self.tabPDF = QtWidgets.QWidget()
        self.tabPDF.setObjectName("tabPDF")
        self.tabWidget.addTab(self.tabPDF, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Preferences)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.label_4.setText(_translate("Preferences", "Title"))
        self.label_8.setText(_translate("Preferences", "Online Dictionary"))
        self.sourceCombo.setItemText(0, _translate("Preferences", "Dictionary.com"))
        self.sourceCombo.setItemText(1, _translate("Preferences", "Wiktionary"))
        self.sourceCombo.setItemText(2, _translate("Preferences", "Cambridge Dictionary"))
        self.sourceCombo.setItemText(3, _translate("Preferences", "Oxford English Dictionary"))
        self.label.setText(_translate("Preferences", "Definitions per Word"))
        self.label_2.setText(_translate("Preferences", "Examples per Definition"))
        self.label_6.setText(_translate("Preferences", "BGM Directory"))
        self.label_5.setText(_translate("Preferences", "SFX Directory"))
        self.label_3.setText(_translate("Preferences", "Working Directory"))
        self.label_7.setText(_translate("Preferences", "Wordlist Directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), _translate("Preferences", "General"))
        self.label_9.setText(_translate("Preferences", "Software"))
        self.label_10.setText(_translate("Preferences", "Current Item to Voice map:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTTS), _translate("Preferences", "TTS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPDF), _translate("Preferences", "PDF"))

