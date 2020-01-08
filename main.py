import sys
from PyQt5.QtWidgets import QApplication, QWidget


class GazeTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setWindowTitle('Gaze Tracker')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GazeTracker()
    sys.exit(app.exec_())
