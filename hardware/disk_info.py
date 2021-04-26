from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_disk_info
    
def display_disk_info(tableWidget):
    disk_info = get_disk_info()
    
    font = QtGui.QFont()
    font.setBold(True)
    
    for key in disk_info:
        if key != 'Partitions and Usage':
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            tableWidget.setItem(rowPosition, 0, info_key)
            info_value = QtWidgets.QTableWidgetItem(str(disk_info[key]))
            tableWidget.setItem(rowPosition, 1, info_value)
    partitions = disk_info['Partitions and Usage']
    for partition in partitions:
        rowPosition = tableWidget.rowCount()
        tableWidget.insertRow(rowPosition)
        
        device_name = partition['Device']
        deviceItem = QtWidgets.QTableWidgetItem(str(f'- {device_name} '))
        deviceItem.setFont(font)
        tableWidget.setItem(rowPosition, 0, deviceItem)
        for key in partition:
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            
            info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
            tableWidget.setItem(rowPosition, 0, info_key)
            info_value = QtWidgets.QTableWidgetItem(str(f'    {partition[key]}'))
            tableWidget.setItem(rowPosition, 1, info_value)

