from PyQt5 import QtCore, QtGui, QtWidgets
from port_scan import Port_scan


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        
        ################################## Home ############################################
        
        self.home = QtWidgets.QWidget()
        
        self.home.setObjectName("home")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.home)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.home)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.stackedWidget.addWidget(self.home)
        ######################################################################################
        
        ########################## Port Scan ##############################
        self.port_scan = QtWidgets.QWidget()
        self.port_scan_ui = Port_scan(self.port_scan)
        self.stackedWidget.addWidget(self.port_scan)
        ######################################################################################

        #################################### Ip Scan #########################################
        self.ip_scan = QtWidgets.QWidget()
        
        self.ip_scan.setObjectName("ip_scan")
        self.label_3 = QtWidgets.QLabel(self.ip_scan)
        self.label_3.setGeometry(QtCore.QRect(300, 190, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.stackedWidget.addWidget(self.ip_scan)
        ######################################################################################

        ################################# Terminal ###########################################
        self.terminal = QtWidgets.QWidget()
        
        self.terminal.setObjectName("terminal")
        self.label_4 = QtWidgets.QLabel(self.terminal)
        self.label_4.setGeometry(QtCore.QRect(230, 210, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.stackedWidget.addWidget(self.terminal)
        ######################################################################################

        self.verticalLayout_3.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave_as = QtWidgets.QMenu(self.menuFile)
        self.menuSave_as.setObjectName("menuSave_as")
        self.menuUtilities = QtWidgets.QMenu(self.menubar)
        self.menuUtilities.setObjectName("menuUtilities")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionJson = QtWidgets.QAction(MainWindow)
        self.actionJson.setObjectName("actionJson")
        
        self.actionPdf = QtWidgets.QAction(MainWindow)
        self.actionPdf.setObjectName("actionPdf")
        self.actionPdf.triggered.connect(self.port_scan_ui.saveAsPdf)
        
        self.actionPorts_scan = QtWidgets.QAction(MainWindow)
        self.actionPorts_scan.setObjectName("actionPorts_scan")
        
        self.actionIp_scan = QtWidgets.QAction(MainWindow)
        self.actionIp_scan.setObjectName("actionIp_scan")
        
        self.actionTerminal = QtWidgets.QAction(MainWindow)
        self.actionTerminal.setObjectName("actionTerminal")
        
        self.menuSave_as.addAction(self.actionJson)
        self.menuSave_as.addAction(self.actionPdf)
        
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuUtilities.addAction(self.actionPorts_scan)
        self.menuUtilities.addAction(self.actionIp_scan)
        self.menuUtilities.addAction(self.actionTerminal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuUtilities.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cerbere"))
        self.label.setText(_translate("MainWindow", "Bienvenue sur notre nouvelle application - Cerbere"))

        self.label_3.setText(_translate("MainWindow", "Ip Scan"))
        self.label_4.setText(_translate("MainWindow", "Terminal"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave_as.setTitle(_translate("MainWindow", "Save as"))
        self.menuUtilities.setTitle(_translate("MainWindow", "Utilities"))
        self.actionJson.setText(_translate("MainWindow", "Json"))
        self.actionPdf.setText(_translate("MainWindow", "Pdf"))
        self.actionPorts_scan.setText(_translate("MainWindow", "Ports scan"))
        self.actionIp_scan.setText(_translate("MainWindow", "Ip scan"))
        self.actionTerminal.setText(_translate("MainWindow", "Terminal"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
