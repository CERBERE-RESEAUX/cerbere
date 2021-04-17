from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_system_info, get_boot_time


class System_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, sysInfo_groupBox):
        sysInfo_groupBox.setGeometry(QtCore.QRect(50, 50, 600, 260))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(sysInfo_groupBox.sizePolicy().hasHeightForWidth())
        sysInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        sysInfo_groupBox.setFont(font)
        sysInfo_groupBox.setStyleSheet("background-color:white")
        sysInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        sysInfo_groupBox.setObjectName("sysInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(sysInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.tableWidget = QtWidgets.QTableWidget(sysInfo_groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.display_system_info()
        
        self.horizontalLayout.addWidget(self.tableWidget)



    def display_system_info(self):
        sys_info = get_system_info()
        boot_time = get_boot_time()
        sys_info['Boot Time'] = boot_time['Boot Time']
        
        font = QtGui.QFont()
        font.setBold(True)

        for key in sys_info:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            self.tableWidget.setItem(rowPosition, 0, info_key)
            
            info_value = QtWidgets.QTableWidgetItem(str(sys_info[key]))
            self.tableWidget.setItem(rowPosition, 1, info_value)

