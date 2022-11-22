from PyQt5 import QtWidgets, QtGui
from PyQt5 import uic
import sys
import random


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)

        self.is_painting = False
        self.pushButton.clicked.connect(self.click_btn)

    def paintEvent(self, event):
        if self.is_painting:
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setPen(QtGui.QColor(255, 191, 0))
            side = random.randrange(201)
            qp.drawEllipse(self.width() // 2, self.height() // 2, side, side, )
            qp.end()

    def click_btn(self):
        self.is_painting = True
        self.pushButton.setVisible(False)
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
