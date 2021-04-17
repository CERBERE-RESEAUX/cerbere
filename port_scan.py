from PyQt5 import QtCore, QtGui, QtWidgets
import nmap
import json
from fpdf import FPDF
import os
from datetime import date


class Port_scan(object):
    
    def __init__(self, root):
        self.scan_data = None
        self.nmScan = nmap.PortScanner()
        self.setupUi(root)

    def setupUi(self, root):
        root.setObjectName("port_scan")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(root)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(root)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        self.ip_label = QtWidgets.QLabel(root)
        self.ip_label.setObjectName("ip_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.ip_label)
        
        self.start_label = QtWidgets.QLabel(root)
        self.start_label.setObjectName("start_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.start_label)
        
        self.end_label = QtWidgets.QLabel(root)
        self.end_label.setObjectName("end_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.end_label)
        
        self.ip_input = QtWidgets.QLineEdit(root)
        self.ip_input.setObjectName("ip_input")
        ip_reg_ex = QtCore.QRegExp("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        ip_input_validator = QtGui.QRegExpValidator(ip_reg_ex, self.ip_input)
        self.ip_input.setValidator(ip_input_validator)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ip_input)
        
        self.start_input = QtWidgets.QLineEdit(root)
        self.start_input.setObjectName("start_input")
        self.start_input.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.start_input)
        
        self.end_input = QtWidgets.QLineEdit(root)
        self.end_input.setObjectName("end_input")
        self.end_input.setValidator(QtGui.QIntValidator())
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.end_input)
        
        self.scan_btn = QtWidgets.QPushButton(root)
        self.scan_btn.setObjectName("scan_btn")
        self.scan_btn.clicked.connect(self.scanPorts)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.scan_btn)
        
        self.verticalLayout_2.addLayout(self.formLayout)
        
        self.tableWidget = QtWidgets.QTableWidget(root)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        
        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", "Port scan"))
        self.ip_label.setText(_translate("MainWindow", "Ip Addresse"))
        self.start_label.setText(_translate("MainWindow", "Start Port"))
        self.end_label.setText(_translate("MainWindow", "End Port"))
        self.scan_btn.setText(_translate("MainWindow", "Scan"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Port"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))

    # get inputs data and scan ports in start_input and end_input interval
    def scanPorts(self):
        self.clearTableWidget()

        ip_addr = self.ip_input.text()
        start_port = self.start_input.text()
        end_port = self.end_input.text()

        interval = start_port + '-' + end_port
        table_data = self.nmScan.scan(ip_addr, interval)
        self.scan_data = table_data['scan'][ip_addr]['tcp']
        
        self.setTableWidgetData()

    # set table widget data
    def setTableWidgetData(self):
        for port in self.scan_data:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(port)))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(self.scan_data[port]['name']))
            self.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(self.scan_data[port]['state']))

    # clear table widget
    def clearTableWidget(self):
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)

    # save table widget content as pdf
    def saveAsPdf(self):
        """ if self.scan_data:
            print('save data as pdf')
        else:
            print('no data available') 
        """
        today = date.today()
        # dd/mm/YY
        d = today.strftime("%d/%m/%Y")

        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(60)
        pdf.cell(75, 10,'Rapport du ' + d, 0, 2, 'C')
        
        pdf.ln(5) 

        # Effective page width, or just epw
        epw = pdf.w - 2*pdf.l_margin

        # Set column width to 1/4 of effective page width to distribute content 
        # evenly across table and page
        col_width = epw/4

        th = pdf.font_size

        pdf.set_font('Times','B',10)
        header = ['port', 'name', 'status']
        pdf.cell(25)
        for h in header:
            pdf.cell(col_width, th, h, border=1, align='C')

        pdf.ln(th)
        # Remember to always put one of these at least once.
        pdf.set_font('Times','',10)

        for port in self.scan_data:
            pdf.cell(25)
            pdf.cell(col_width, th, str(port), border=1, align='C')
            pdf.cell(col_width, th, self.scan_data[port]['name'], border=1, align='C')
            pdf.cell(col_width, th, self.scan_data[port]['state'], border=1, align='C')
            pdf.ln(th)
            

        pdf.output(os.getenv('HOME') + '/tuto1.pdf', 'F')
