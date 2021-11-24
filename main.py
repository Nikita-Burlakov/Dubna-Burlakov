import sys

from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

from random import choice


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for i in range(choice(range(1, 121))):
                x, y = choice(range(1, 801)), choice(range(1, 601))
                rad = choice(range(1, 100))
                #
                red, green, blue = choice(range(256)), choice(range(256)),\
                                   choice(range(256))
                qp.setBrush(QColor(red, green, blue))
                #
                qp.drawEllipse(x, y, rad, rad)
            self.do_paint = False
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
