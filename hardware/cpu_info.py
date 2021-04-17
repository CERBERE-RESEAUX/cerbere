from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_cpu_info

class Cpu_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, cpuInfo_groupBox):
        cpuInfo_groupBox.setGeometry(QtCore.QRect(470, 520, 400, 445))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(cpuInfo_groupBox.sizePolicy().hasHeightForWidth())
        cpuInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        cpuInfo_groupBox.setFont(font)
        cpuInfo_groupBox.setStyleSheet("background-color:white")
        cpuInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        cpuInfo_groupBox.setObjectName("cpuInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(cpuInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.tableWidget = QtWidgets.QTableWidget(cpuInfo_groupBox)
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

        self.display_cpu_info()

        self.horizontalLayout.addWidget(self.tableWidget)

    
    def display_cpu_info(self):
        cpu_info = get_cpu_info()
        
        font = QtGui.QFont()
        font.setBold(True)

        for key in cpu_info:
            if key != 'CPU Usage Per Core':
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
                info_key.setFont(font)
                self.tableWidget.setItem(rowPosition, 0, info_key)
                info_value = QtWidgets.QTableWidgetItem(str(cpu_info[key]))
                self.tableWidget.setItem(rowPosition, 1, info_value)
            else:
                cors = cpu_info['CPU Usage Per Core']

                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)

                item = QtWidgets.QTableWidgetItem(str(f'- CPU Usage Per Core '))
                item.setFont(font)
                self.tableWidget.setItem(rowPosition, 0, item)

                for key in cors:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)

                    info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
                    self.tableWidget.setItem(rowPosition, 0, info_key)

                    info_value = QtWidgets.QTableWidgetItem(str(f'    {cors[key]}'))
                    self.tableWidget.setItem(rowPosition, 1, info_value)