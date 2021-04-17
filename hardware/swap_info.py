from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_swap_info


class Swap_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, swapInfo_groupBox):
        swapInfo_groupBox.setGeometry(QtCore.QRect(350, 320, 290, 175))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(swapInfo_groupBox.sizePolicy().hasHeightForWidth())
        swapInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        swapInfo_groupBox.setFont(font)
        swapInfo_groupBox.setStyleSheet("background-color:white")
        swapInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        swapInfo_groupBox.setObjectName("swapInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(swapInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.tableWidget = QtWidgets.QTableWidget(swapInfo_groupBox)
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

        self.display_swap_info()
        
        self.horizontalLayout.addWidget(self.tableWidget)



    def display_swap_info(self):
        swap_info = get_swap_info()
        
        font = QtGui.QFont()
        font.setBold(True)

        for key in swap_info:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            self.tableWidget.setItem(rowPosition, 0, info_key)
            
            info_value = QtWidgets.QTableWidgetItem(str(swap_info[key]))
            self.tableWidget.setItem(rowPosition, 1, info_value)
