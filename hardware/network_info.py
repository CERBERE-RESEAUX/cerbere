from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_network_info


class Network_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, networkInfo_groupBox):
        networkInfo_groupBox.setGeometry(QtCore.QRect(700, 50, 400, 445))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(networkInfo_groupBox.sizePolicy().hasHeightForWidth())
        networkInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        networkInfo_groupBox.setFont(font)
        networkInfo_groupBox.setStyleSheet("background-color:white")
        networkInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        networkInfo_groupBox.setObjectName("networkInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(networkInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.tableWidget = QtWidgets.QTableWidget(networkInfo_groupBox)
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

        self.display_network_info()

        self.horizontalLayout.addWidget(self.tableWidget)



    def display_network_info(self):
        network_info = get_network_info()
        
        font = QtGui.QFont()
        font.setBold(True)

        for key in network_info:
            if key != 'Interfaces':
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)

                info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
                info_key.setFont(font)
                self.tableWidget.setItem(rowPosition, 0, info_key)

                info_value = QtWidgets.QTableWidgetItem(str(network_info[key]))
                self.tableWidget.setItem(rowPosition, 1, info_value)

        interfaces = network_info['Interfaces']

        for interface in interfaces:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            interface_name = interface['Interface']
            interfaceName = QtWidgets.QTableWidgetItem(str(f'- {interface_name} '))
            interfaceName.setFont(font)
            self.tableWidget.setItem(rowPosition, 0, interfaceName)

            for key in interface:
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                
                info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
                self.tableWidget.setItem(rowPosition, 0, info_key)

                info_value = QtWidgets.QTableWidgetItem(str(f'    {interface[key]}'))
                self.tableWidget.setItem(rowPosition, 1, info_value)
