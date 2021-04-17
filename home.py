from PyQt5 import QtCore, QtGui, QtWidgets
from hardware.system_info import System_info
from hardware.memory_info import Memory_info
from hardware.swap_info import Swap_info
from hardware.network_info import Network_info
from hardware.disk_info import Disk_info
from hardware.cpu_info import Cpu_info

class Home(object):
    def __init__(self, root):
        self.setupUi(root)


    def setupUi(self, home):
        home.setObjectName("home")

        self.sysInfo_groupBox = QtWidgets.QGroupBox(home)
        self.sysInfo_groupBox.setTitle('System Information')
        System_info(self.sysInfo_groupBox)

        self.memoryInfo_groupBox = QtWidgets.QGroupBox(home)
        self.memoryInfo_groupBox.setTitle('Memory Information')
        Memory_info(self.memoryInfo_groupBox)

        self.swapInfo_groupBox = QtWidgets.QGroupBox(home)
        self.swapInfo_groupBox.setTitle('Swap Information')
        Swap_info(self.swapInfo_groupBox)

        self.networkInfo_groupBox = QtWidgets.QGroupBox(home)
        self.networkInfo_groupBox.setTitle('Network Information')
        Network_info(self.networkInfo_groupBox)

        self.diskInfo_groupBox = QtWidgets.QGroupBox(home)
        self.diskInfo_groupBox.setTitle('Disk Information')
        Disk_info(self.diskInfo_groupBox)

        self.cpuInfo_groupBox = QtWidgets.QGroupBox(home)
        self.cpuInfo_groupBox.setTitle('CPU Information')
        Cpu_info(self.cpuInfo_groupBox)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Form"))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QWidget()
    ui = Home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
