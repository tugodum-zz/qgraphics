import sys, math  # For argv
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QGradient, QLinearGradient, QPen, QBrush, QColor, QPainter, QPolygonF
from PySide6.QtCore import QPoint, QRect, QRectF, QPointF, QTimer, Qt

class MainApp(QtWidgets.QMainWindow):
    resized = QtCore.Signal()

    segAPoints = [
        QPointF(0.0, 0.6), QPointF(0.1, 0.25), QPointF(0.25, 0.0),
        QPointF(1.0, 0.0), QPointF(0.9, 1.0), QPointF(0.4, 1.0),
        QPointF(0.0, 0.6)
    ]

    segBPoints = [
        QPointF(0.5, 0.0), QPointF(0.75, 0.1), QPointF(1.0, 0.25),
        QPointF(0.9, 0.8), QPointF(0.65, 1.0), QPointF(0.0, 0.8),
        QPointF(0.12, 0.25)
    ]

    segCPoints = [
        QPointF(0.75, 0.0), QPointF(1.0, 0.2), QPointF(0.9, 0.75),
        QPointF(0.75, 0.9), QPointF(0.5, 1.0), QPointF(0.0, 0.75),
        QPointF(0.12, 0.2)
    ]

    def __init__(self):
        super().__init__()
        self.polygons = []
        self.pen = QPen(Qt.green)                      # set lineColor
        self.pen.setWidth(1)                                            # set lineWidth
        self.brush = QBrush(Qt.green)        # set fillColor  
        self.polygons.append(self.createPoly(QRectF(10, 10, 200, 50), self.segAPoints)) # polygon with n points, radius, angle of the first point
        self.polygons.append(self.createPoly(QRectF(200, 10, 60, 200), self.segBPoints)) # polygon with n points, radius, angle of the first point
        self.polygons.append(self.createPoly(QRectF(190, 220, 60, 200), self.segCPoints)) # polygon with n points, radius, angle of the first point

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
        for polygon in self.polygons:
            painter.drawPolygon(polygon)

    def createPoly(self, boundingBox, polyPoints):
        polygon = QtGui.QPolygonF()
        for point in polyPoints: 
            polygon.append(QPointF(point.x() * boundingBox.width(), point.y() * boundingBox.height()))  
        polygon.translate(boundingBox.topLeft())
        return polygon

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()

    window.setWindowTitle("Play with Graphics")

    window.show()
    app.exec()

if __name__ == '__main__':
    main()
    