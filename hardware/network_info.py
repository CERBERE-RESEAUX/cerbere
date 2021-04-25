from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_network_info

def display_network_info(tableWidget):
    network_info = get_network_info()
    
    font = QtGui.QFont()
    font.setBold(True)
    for key in network_info:
        if key != 'Interfaces':
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            tableWidget.setItem(rowPosition, 0, info_key)
            info_value = QtWidgets.QTableWidgetItem(str(network_info[key]))
            tableWidget.setItem(rowPosition, 1, info_value)
    interfaces = network_info['Interfaces']
    for interface in interfaces:
        rowPosition = tableWidget.rowCount()
        tableWidget.insertRow(rowPosition)
        interface_name = interface['Interface']
        interfaceName = QtWidgets.QTableWidgetItem(str(f'- {interface_name} '))
        interfaceName.setFont(font)
        tableWidget.setItem(rowPosition, 0, interfaceName)
        for key in interface:
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            
            info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
            tableWidget.setItem(rowPosition, 0, info_key)
            info_value = QtWidgets.QTableWidgetItem(str(f'    {interface[key]}'))
            tableWidget.setItem(rowPosition, 1, info_value)
