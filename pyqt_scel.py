import sys  # For argv
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QGradient, QLinearGradient, QPen, QBrush
from PySide6.QtCore import QPoint, QRect, QRectF, QTimer, Qt
from <place your design file name here> import Ui_MainWindow  # Import design

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    resized = QtCore.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate

        self.connectSignals()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainApp, self).resizeEvent(event)

    def connectSignals(self):
        # Connect your signals here like:
        self.resized.connect(self.onResize)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.setWindowTitle("Play with Graphics")

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
    