from PyQt5 import QtCore, QtGui, QtWidgets
from utils.hardware import get_cpu_info

    
def display_cpu_info(tableWidget):
    cpu_info = get_cpu_info()
    
    font = QtGui.QFont()
    font.setBold(True)
    for key in cpu_info:
        if key != 'CPU Usage Per Core':
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            info_key = QtWidgets.QTableWidgetItem(str(f'{key} : '))
            info_key.setFont(font)
            tableWidget.setItem(rowPosition, 0, info_key)
            info_value = QtWidgets.QTableWidgetItem(str(cpu_info[key]))
            tableWidget.setItem(rowPosition, 1, info_value)
        else:
            cors = cpu_info['CPU Usage Per Core']
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            item = QtWidgets.QTableWidgetItem(str(f'- CPU Usage Per Core '))
            item.setFont(font)
            tableWidget.setItem(rowPosition, 0, item)
            for key in cors:
                rowPosition = tableWidget.rowCount()
                tableWidget.insertRow(rowPosition)
                info_key = QtWidgets.QTableWidgetItem(str(f'    {key} : '))
                tableWidget.setItem(rowPosition, 0, info_key)
                info_value = QtWidgets.QTableWidgetItem(str(f'    {cors[key]}'))
                tableWidget.setItem(rowPosition, 1, info_value)