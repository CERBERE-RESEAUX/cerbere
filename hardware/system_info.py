from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_system_info, get_boot_time

def display_system_info(tableWidget):
    sys_info = get_system_info()
    boot_time = get_boot_time()
    sys_info['Boot Time'] = boot_time['Boot Time']
    
    font = QtGui.QFont()
    font.setBold(True)
    for key in sys_info:
        rowPosition = tableWidget.rowCount()
        tableWidget.insertRow(rowPosition)
        info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
        info_key.setFont(font)
        tableWidget.setItem(rowPosition, 0, info_key)
        
        info_value = QtWidgets.QTableWidgetItem(str(sys_info[key]))
        tableWidget.setItem(rowPosition, 1, info_value)

