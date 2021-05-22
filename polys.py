import sys  # For argv
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QGradient, QLinearGradient, QPen, QBrush, QColor, QPainter
from PySide6.QtCore import QPoint, QRect, QRectF, QTimer, Qt

class MainApp(QtWidgets.QMainWindow):
    resized = QtCore.Signal()
    def __init__(self):
        super().__init__()
        
        self.pen = QPen(QColor(0,0,0))                      # set lineColor
        self.pen.setWidth(3)                                            # set lineWidth
        self.brush = QBrush(QColor(255,255,255,255))        # set fillColor  
        self.polygon = self.createPoly(8,150,0)                         # polygon with n points, radius, angle of the first point

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainApp, self).resizeEvent(event)

    def connectSignals(self):
        # Connect your signals here like:
        self.resized.connect(self.onResize)
      
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)  
        painter.drawPolygon(self.polygon)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.setWindowTitle("Play with Graphics")

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
    