# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translator_ui.ui'
#
# Created: Tue Feb 04 03:49:22 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.originalTextBox = QtGui.QTextEdit(Dialog)
        self.originalTextBox.setGeometry(QtCore.QRect(10, 20, 521, 161))
        self.originalTextBox.setObjectName("originalTextBox")
        self.translatedTextBox = QtGui.QTextEdit(Dialog)
        self.translatedTextBox.setGeometry(QtCore.QRect(10, 200, 521, 141))
        self.translatedTextBox.setObjectName("translatedTextBox")
        self.translateButton = QtGui.QPushButton(Dialog)
        self.translateButton.setGeometry(QtCore.QRect(10, 350, 521, 61))
        self.translateButton.setObjectName("translateButton")
        self.originalTextLabel = QtGui.QLabel(Dialog)
        self.originalTextLabel.setGeometry(QtCore.QRect(10, 0, 101, 16))
        self.originalTextLabel.setObjectName("originalTextLabel")
        self.translateLabel = QtGui.QLabel(Dialog)
        self.translateLabel.setGeometry(QtCore.QRect(10, 180, 111, 16))
        self.translateLabel.setObjectName("translateLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The FDA-ter Translator", None, QtGui.QApplication.UnicodeUTF8))
        self.translateButton.setText(QtGui.QApplication.translate("Dialog", "Translate to FDA Speak", None, QtGui.QApplication.UnicodeUTF8))
        self.originalTextLabel.setText(QtGui.QApplication.translate("Dialog", "Original Text", None, QtGui.QApplication.UnicodeUTF8))
        self.translateLabel.setText(QtGui.QApplication.translate("Dialog", "Translated Text", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
