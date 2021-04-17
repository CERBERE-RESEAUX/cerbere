from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_memory_info


class Memory_info(object):
    def __init__(self, root):
        self.setupUi(root)

    def setupUi(self, memoryInfo_groupBox):
        memoryInfo_groupBox.setGeometry(QtCore.QRect(50, 320, 290, 175))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(memoryInfo_groupBox.sizePolicy().hasHeightForWidth())
        memoryInfo_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        memoryInfo_groupBox.setFont(font)
        memoryInfo_groupBox.setStyleSheet("background-color:white")
        memoryInfo_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        memoryInfo_groupBox.setObjectName("memoryInfo_groupBox")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(memoryInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.tableWidget = QtWidgets.QTableWidget(memoryInfo_groupBox)
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

        self.display_memory_info()
        
        self.horizontalLayout.addWidget(self.tableWidget)



    def display_memory_info(self):
        memory_info = get_memory_info()
        
        font = QtGui.QFont()
        font.setBold(True)

        for key in memory_info:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            self.tableWidget.setItem(rowPosition, 0, info_key)
            
            info_value = QtWidgets.QTableWidgetItem(str(memory_info[key]))
            self.tableWidget.setItem(rowPosition, 1, info_value)
