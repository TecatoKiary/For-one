from PyQt5 import QtWidgets, QtGui
import sys
import random
from UI import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.obj = Ui_MainWindow()  # Эксперимент: использовать в другом файле
        self.obj.setupUi(self)
        # Вывод: очень неудобно
        self.is_painting = False
        self.obj.pushButton.clicked.connect(self.click_btn)

    def paintEvent(self, event):
        if self.is_painting:
            qp = QtGui.QPainter()
            qp.begin(self)
            qp.setPen(QtGui.QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
            side = random.randrange(201)
            qp.drawEllipse(self.width() // 2, self.height() // 2, side, side, )
            qp.end()

    def click_btn(self):
        self.is_painting = True
        self.obj.pushButton.setVisible(False)
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
