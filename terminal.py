from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys
import os

class Terminal(object):

    def __init__(self, root):
        self.setupUi(root)
        self.working_dir = "."


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 635)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.lineEdit.returnPressed.connect(self.doCMD)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def doCMD(self):
        cmd = self.lineEdit.text()
        self.lineEdit.setText("")

        if "cd " in cmd:
            vals = cmd.split(" ")
            if vals[1][0] == "/":
                self.working_dir = vals[1]
            else:
                self.working_dir = self.working_dir + "/" + vals[1]

            print(self.working_dir)
                
            subprocess.call(cmd, shell=True, cwd=self.working_dir)
            self.textBrowser.setText( self.textBrowser.toPlainText() + "\n$ " + cmd )
        else:
            result = subprocess.check_output(cmd, shell=True, cwd=self.working_dir)
            self.textBrowser.setText( self.textBrowser.toPlainText() + "\n$ " + cmd + result.decode("utf-8")  )
        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())
