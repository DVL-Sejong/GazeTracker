# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel

from objects.object import Point


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1886, 1338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(255, 170, 255)")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.brun = QtWidgets.QPushButton(self.widget)
        self.brun.setObjectName("brun")
        self.gridLayout_2.addWidget(self.brun, 0, 0, 1, 1)
        self.bend = QtWidgets.QPushButton(self.widget)
        self.bend.setObjectName("bend")
        self.gridLayout_2.addWidget(self.bend, 0, 1, 1, 1)
        self.bvisible = QtWidgets.QPushButton(self.widget)
        self.bvisible.setObjectName("bvisible")
        self.gridLayout_2.addWidget(self.bvisible, 0, 2, 1, 1)
        self.bunvisible = QtWidgets.QPushButton(self.widget)
        self.bunvisible.setObjectName("bunvisible")
        self.gridLayout_2.addWidget(self.bunvisible, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(1287, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.paint = Paint(self.centralwidget)
        self.paint.setStyleSheet("background-color: rgb(194, 221, 255)")
        self.paint.setText("")
        self.paint.setObjectName("paint")
        self.verticalLayout.addWidget(self.paint)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1886, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.brun.setText(_translate("MainWindow", "run"))
        self.bend.setText(_translate("MainWindow", "end"))
        self.bvisible.setText(_translate("MainWindow", "visible"))
        self.bunvisible.setText(_translate("MainWindow", "unvisible"))


class Paint(QLabel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.points = []
        self.left = Point(0, 0, 0)
        self.right = Point(0, 0, 0)

    def paintEvent(self, e):
        super().paintEvent(e)
        if self.left.validity is 0 or self.right.validity is 0: return
        self.points.append(self.left)

        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        pen = QtGui.QPen(QtCore.Qt.red, 5)
        brush = QtGui.QBrush(QtCore.Qt.red)
        qp.setPen(pen)
        qp.setBrush(brush)

        for point in self.points:
            qp.drawEllipse(point.x, point.y, 5, 5)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
