import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainWindow import Ui_MainWindow

class Main:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        self.ui.nav_home_btn.clicked.connect(self.showHome)
        self.ui.nav_scan_btn.clicked.connect(self.showPortScan)
        self.ui.nav_ip_btn.clicked.connect(self.showIpScan)
        self.ui.nav_terminal_btn.clicked.connect(self.showTerminal)

    
    def show(self):
        self.main_win.showMaximized()

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def showPortScan(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.port_scan)
    
    def showIpScan(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ip_scan)

    def showTerminal(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.terminal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    sys.exit(app.exec_())