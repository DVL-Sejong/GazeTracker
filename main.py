import sys
from operator import eq
from time import sleep

import pyautogui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow

from Tobii import Tobii
from MainWindow import Ui_MainWindow
from database import constant as dbconstant
from objects import constant
from database.lib import MYSQL
from objects.GazeData import GazeData


class GazeTracker(QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = GazeData(self)
        self.resized.connect(self.synchronize_geometries)
        self.connectSlots()
        self.tobii = Tobii(self)

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

    def connectSlots(self):
        self.brun.clicked.connect(self.on_click)
        self.bend.clicked.connect(self.on_click)

    def save(self):
        dbconn = MYSQL(
            dbhost=dbconstant.HOST,
            dbuser=dbconstant.USER,
            dbpwd=dbconstant.PASSWORD,
            dbname=dbconstant.DB_NAME,
            dbcharset=dbconstant.CHARSET
        )

        ex.data.save(dbconn)
        dbconn.close()

    @pyqtSlot()
    def on_click(self):
        sending_button = self.sender()
        if eq(sending_button.objectName(), "brun"):
            self.brun.setEnabled(False)
            self.bend.setEnabled(True)
            self.tobii.run()
        elif eq(sending_button.objectName(), "bend"):
            self.brun.setEnabled(True)
            self.bend.setEnabled(False)
            self.tobii.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GazeTracker()
    ex.show()
    ex.synchronize_geometries()
    sys.exit(app.exec_())
