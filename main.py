import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygon, QPen
from PyQt5.QtWidgets import QWidget, QApplication

import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        self.d = False
        uic.loadUi('rep1.ui', self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(1000, 1000)
        self.pushButton.clicked.connect(self.btnpush)
        self.show()

    def btnpush(self):
        self.d = True
        self.update()

    def paintEvent(self, e):
        if self.d:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        brush = QBrush(Qt.SolidPattern)
        dia = random.randint(20, 500)
        brush.setColor(QColor(255, 255, 0))
        qp.setBrush(brush)
        x = random.randint(100, 500)
        y = random.randint(100, 500)

        qp.drawEllipse(x, y, x - dia // 2, y - dia // 2)

        self.d = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
