import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 100, 750, 600)
        self.tableWidget.resize(620, 300)
        #
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.data = self.cur.execute('SELECT * FROM coffee').fetchall()
        #
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        title = ('Сорт', 'Степень обжарки', 'Молотый / в зёрнах',
                 'Вкус', 'Цена (руб.)', 'Объём упаковки (л)')
        self.tableWidget.setHorizontalHeaderLabels(title)
        #
        for i, row in enumerate(self.data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row[1:]):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
