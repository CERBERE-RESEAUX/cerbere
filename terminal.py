from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import subprocess
 
class termcerbere(QtWidgets.QMainWindow):
    def __init__(self):
        super(termcerbere, self).__init__()
        uic.loadUi('gui.ui', self)
        self.lineEdit.returnPressed.connect(self.doCMD)
        #self.pushButtonInstall.clicked.connect(self.onClick)
        self.working_dir = "."
        
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
    
app = QtWidgets.QApplication([])
win = termcerbere()
win.show()
sys.exit(app.exec())