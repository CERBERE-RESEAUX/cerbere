from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_swap_info

def display_swap_info(tableWidget):
    swap_info = get_swap_info()
    
    font = QtGui.QFont()
    font.setBold(True)
    for key in swap_info:
        rowPosition = tableWidget.rowCount()
        tableWidget.insertRow(rowPosition)
        info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
        info_key.setFont(font)
        tableWidget.setItem(rowPosition, 0, info_key)
        
        info_value = QtWidgets.QTableWidgetItem(str(swap_info[key]))
        tableWidget.setItem(rowPosition, 1, info_value)
