from PyQt5 import QtCore, QtGui, QtWidgets
from port_scan import Port_scan
from home import Home
from terminal import Terminal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1052, 664)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.nav_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nav_widget.sizePolicy().hasHeightForWidth())
        self.nav_widget.setSizePolicy(sizePolicy)
        self.nav_widget.setStyleSheet("background-color:#057EAB")
        self.nav_widget.setObjectName("nav_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.nav_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nav_menu_label_2 = QtWidgets.QLabel(self.nav_widget)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.nav_menu_label_2.setFont(font)
        self.nav_menu_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nav_menu_label_2.setObjectName("nav_menu_label_2")
        self.verticalLayout_2.addWidget(self.nav_menu_label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.nav_home_btn = QtWidgets.QPushButton(self.nav_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nav_home_btn.setFont(font)
        self.nav_home_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_home_btn.setStyleSheet("border:none")
        self.nav_home_btn.setObjectName("nav_home_btn")
        self.verticalLayout_2.addWidget(self.nav_home_btn)
        self.nav_line1_2 = QtWidgets.QFrame(self.nav_widget)
        self.nav_line1_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.nav_line1_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nav_line1_2.setObjectName("nav_line1_2")
        self.verticalLayout_2.addWidget(self.nav_line1_2)
        self.nav_scan_btn = QtWidgets.QPushButton(self.nav_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nav_scan_btn.setFont(font)
        self.nav_scan_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_scan_btn.setStyleSheet("border:none")
        self.nav_scan_btn.setObjectName("nav_scan_btn")
        self.verticalLayout_2.addWidget(self.nav_scan_btn)
        self.nav_line2_2 = QtWidgets.QFrame(self.nav_widget)
        self.nav_line2_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.nav_line2_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nav_line2_2.setObjectName("nav_line2_2")
        self.verticalLayout_2.addWidget(self.nav_line2_2)
        self.nav_ip_btn = QtWidgets.QPushButton(self.nav_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nav_ip_btn.setFont(font)
        self.nav_ip_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_ip_btn.setStyleSheet("border:none")
        self.nav_ip_btn.setObjectName("nav_ip_btn")
        self.verticalLayout_2.addWidget(self.nav_ip_btn)
        self.nav_line3_2 = QtWidgets.QFrame(self.nav_widget)
        self.nav_line3_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.nav_line3_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.nav_line3_2.setObjectName("nav_line3_2")
        self.verticalLayout_2.addWidget(self.nav_line3_2)
        self.nav_terminal_btn = QtWidgets.QPushButton(self.nav_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nav_terminal_btn.setFont(font)
        self.nav_terminal_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nav_terminal_btn.setStyleSheet("border:none")
        self.nav_terminal_btn.setObjectName("nav_terminal_btn")
        self.verticalLayout_2.addWidget(self.nav_terminal_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.nav_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        
        ################################# Home #################################
        """ 
        self.home.setWidgetResizable(True) """
        self.home = QtWidgets.QWidget()
        self.home_ui = Home(self.home)
        self.stackedWidget.addWidget(self.home)
        #########################################################################
        
        ################################# Port Scan #############################
        self.port_scan = QtWidgets.QWidget()
        self.port_scan_ui = Port_scan(self.port_scan)
        self.stackedWidget.addWidget(self.port_scan)
        #########################################################################

        self.ip_scan = QtWidgets.QWidget()
        self.ip_scan.setObjectName("ip_scan")
        self.label_7 = QtWidgets.QLabel(self.ip_scan)
        self.label_7.setGeometry(QtCore.QRect(300, 10, 67, 17))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.ip_scan)
        
        #################################### Terminal ##########################
        self.terminal = QtWidgets.QWidget()
        self.terminal_ui = Terminal(self.terminal)
        self.stackedWidget.addWidget(self.terminal)
        #######################################################################

        ################################### Menu Bar ############################
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave_as = QtWidgets.QMenu(self.menuFile)
        self.menuSave_as.setObjectName("menuSave_as")
        self.menuSave_as.setTitle('Save As')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionJson = QtWidgets.QAction(MainWindow)
        self.actionJson.setObjectName("actionJson")
        self.actionJson.setText('JSON')
        self.actionJson.triggered.connect(self.port_scan_ui.saveAsJson)

        self.actionPdf = QtWidgets.QAction(MainWindow)
        self.actionPdf.setObjectName("actionPdf")
        self.actionPdf.setText('PDF')
        self.actionPdf.triggered.connect(self.port_scan_ui.saveAsPdf)

        self.menuSave_as.addAction(self.actionJson)
        self.menuSave_as.addAction(self.actionPdf)


        self.menuFile.addAction(self.menuSave_as.menuAction())

        self.menubar.addAction(self.menuFile.menuAction())

        #########################################################################

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nav_menu_label_2.setText(_translate("MainWindow", "Menu"))
        self.nav_home_btn.setText(_translate("MainWindow", "Home"))
        self.nav_scan_btn.setText(_translate("MainWindow", "Port Scan"))
        self.nav_ip_btn.setText(_translate("MainWindow", "IP Scan"))
        self.nav_terminal_btn.setText(_translate("MainWindow", "Terminal"))
        self.label_7.setText(_translate("MainWindow", "IP Scan"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
