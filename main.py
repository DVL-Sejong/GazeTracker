import sys
from time import sleep

import pyautogui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from Tobii import Tobii
from MainWindow import Ui_MainWindow
from database import constant
from database.lib import MYSQL
from objects.GazeData import GazeData


class GazeTracker(QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = GazeData(self)
        self.resized.connect(self.synchronize_geometries)
        self.synchronize_geometries()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(GazeTracker, self).resizeEvent(event)

    def synchronize_geometries(self):
        window = pyautogui.size()
        self.data.synchronize_geometries(window, self.geometry(), self.paint)

    def plot(self, tuple):
        self.data.add_tuple(tuple)

        if self.data.data[-1].is_validate(constant.LEFT) and self.data.data[-1].is_validate(constant.RIGHT):
            self.paint.left = self.data.data[-1].left_point
            self.paint.right = self.data.data[-1].right_point
            self.paint.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GazeTracker()
    ex.show()
    ex.synchronize_geometries()

    tobii = Tobii(ex)
    tobii.run()
    sleep(5)
    tobii.end()
    ex.data.order_in_time()

    dbconn = MYSQL(
        dbhost=constant.HOST,
        dbuser=constant.USER,
        dbpwd=constant.PASSWORD,
        dbname=constant.DB_NAME,
        dbcharset=constant.CHARSET
    )

    ex.data.save(dbconn)
    dbconn.close()

    sys.exit(app.exec_())