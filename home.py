from PyQt5 import QtCore, QtGui, QtWidgets
from hardware.system_info import display_system_info
from hardware.memory_info import display_memory_info
from hardware.cpu_info import display_cpu_info
from hardware.network_info import display_network_info
from hardware.disk_info import display_disk_info
from hardware.swap_info import display_swap_info

class Home(object):
    def __init__(self, root):
        self.setupUi(root)


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 797)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 770, 777))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        font = QtGui.QFont()
        font.setPointSize(13)

        ########################## Logo ##################################

        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_0 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_0.setObjectName("horizontalLayout_0")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui_files/../assets/MicrosoftTeams-image.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_0.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        
        ########################## System info ############################
        self.sysInfo_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.sysInfo_groupBox.setMinimumSize(QtCore.QSize(0, 260))
        self.sysInfo_groupBox.setObjectName("sysInfo_groupBox") 
        self.sysInfo_groupBox.setFont(font)
        self.sysInfo_groupBox.setTitle('System information')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sysInfo_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.sysInfo_groupBox)
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

        display_system_info(self.tableWidget)

        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.sysInfo_groupBox)

        ############################ Memory info #######################################
        self.memory_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.memory_groupBox.setMinimumSize(QtCore.QSize(0, 170))
        self.memory_groupBox.setObjectName("memory_groupBox")
        self.memory_groupBox.setFont(font)
        self.memory_groupBox.setTitle('Memory information')
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.memory_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.memory_groupBox)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)

        header_2 = self.tableWidget_2.horizontalHeader()
        header_2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().hide()
        self.tableWidget_2.verticalHeader().hide()
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        display_memory_info(self.tableWidget_2)

        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.verticalLayout.addWidget(self.memory_groupBox)

        ############################ CPU info #######################################
                
        self.cpu_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.cpu_groupBox.setMinimumSize(QtCore.QSize(0, 500))
        self.cpu_groupBox.setObjectName("cpu_groupBox")
        self.cpu_groupBox.setFont(font)
        self.cpu_groupBox.setTitle('CPU information')
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.cpu_groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.cpu_groupBox)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)

        header_3 = self.tableWidget_3.horizontalHeader()
        header_3.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_3.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_3.horizontalHeader().hide()
        self.tableWidget_3.verticalHeader().hide()
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        display_cpu_info(self.tableWidget_3)

        self.horizontalLayout_3.addWidget(self.tableWidget_3)
        self.verticalLayout.addWidget(self.cpu_groupBox)

        ############################ Network info #######################################
        
        self.network_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.network_groupBox.setMinimumSize(QtCore.QSize(0, 600))
        self.network_groupBox.setObjectName("network_groupBox")
        self.network_groupBox.setFont(font)
        self.network_groupBox.setTitle('Network information')
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.network_groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.network_groupBox)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)

        header_4 = self.tableWidget_4.horizontalHeader()
        header_4.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_4.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_4.horizontalHeader().hide()
        self.tableWidget_4.verticalHeader().hide()
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget_4.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        display_network_info(self.tableWidget_4)

        self.horizontalLayout_4.addWidget(self.tableWidget_4)
        self.verticalLayout.addWidget(self.network_groupBox)

        ############################ Disk info #######################################
        
        self.disk_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.disk_groupBox.setMinimumSize(QtCore.QSize(0, 800))
        self.disk_groupBox.setObjectName("disk_groupBox")
        self.disk_groupBox.setFont(font)
        self.disk_groupBox.setTitle('Network information')
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.disk_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.disk_groupBox)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(0)

        header_5 = self.tableWidget_5.horizontalHeader()
        header_5.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_5.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_5.horizontalHeader().hide()
        self.tableWidget_5.verticalHeader().hide()
        self.tableWidget_5.setShowGrid(False)
        self.tableWidget_5.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget_5.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        display_disk_info(self.tableWidget_5)

        self.horizontalLayout_5.addWidget(self.tableWidget_5)
        self.verticalLayout.addWidget(self.disk_groupBox)

        ############################ Memory info #######################################
        
        self.swap_groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.swap_groupBox.setMinimumSize(QtCore.QSize(0, 180))
        self.swap_groupBox.setObjectName("swap_groupBox")
        self.swap_groupBox.setFont(font)
        self.swap_groupBox.setTitle('Network information')
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.swap_groupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.swap_groupBox)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setRowCount(0)

        header_6 = self.tableWidget_6.horizontalHeader()
        header_6.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_6.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_6.horizontalHeader().hide()
        self.tableWidget_6.verticalHeader().hide()
        self.tableWidget_6.setShowGrid(False)
        self.tableWidget_6.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.tableWidget_6.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        display_swap_info(self.tableWidget_6)

        self.horizontalLayout_6.addWidget(self.tableWidget_6)
        self.verticalLayout.addWidget(self.swap_groupBox)
        

        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


