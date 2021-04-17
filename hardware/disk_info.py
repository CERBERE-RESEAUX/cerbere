from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_disk_info

class Disk_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, diskInfo_groupBox):
        diskInfo_groupBox.setGeometry(QtCore.QRect(50, 520, 400, 445))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(diskInfo_groupBox.sizePolicy().hasHeightForWidth())
        diskInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        diskInfo_groupBox.setFont(font)
        diskInfo_groupBox.setStyleSheet("background-color:white")
        diskInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        diskInfo_groupBox.setObjectName("diskInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(diskInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.tableWidget = QtWidgets.QTableWidget(diskInfo_groupBox)
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

        self.display_disk_info()

        self.horizontalLayout.addWidget(self.tableWidget)

    
    
    def display_disk_info(self):
        disk_info = get_disk_info()
        
        font = QtGui.QFont()
        font.setBold(True)
        
        for key in disk_info:
            if key != 'Partitions and Usage':
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
                info_key.setFont(font)
                self.tableWidget.setItem(rowPosition, 0, info_key)
                info_value = QtWidgets.QTableWidgetItem(str(disk_info[key]))
                self.tableWidget.setItem(rowPosition, 1, info_value)

        partitions = disk_info['Partitions and Usage']

        for partition in partitions:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            
            device_name = partition['Device']
            deviceItem = QtWidgets.QTableWidgetItem(str(f'- {device_name} '))
            deviceItem.setFont(font)
            self.tableWidget.setItem(rowPosition, 0, deviceItem)

            for key in partition:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                
                info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
                self.tableWidget.setItem(rowPosition, 0, info_key)

                info_value = QtWidgets.QTableWidgetItem(str(f'    {partition[key]}'))
                self.tableWidget.setItem(rowPosition, 1, info_value)

