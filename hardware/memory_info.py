from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_memory_info

def display_memory_info(tableWidget):
    memory_info = get_memory_info()
    
    font = QtGui.QFont()
    font.setBold(True)
    for key in memory_info:
        rowPosition = tableWidget.rowCount()
        tableWidget.insertRow(rowPosition)
        info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
        info_key.setFont(font)
        tableWidget.setItem(rowPosition, 0, info_key)
        
        info_value = QtWidgets.QTableWidgetItem(str(memory_info[key]))
        tableWidget.setItem(rowPosition, 1, info_value)
