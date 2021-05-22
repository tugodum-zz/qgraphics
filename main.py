import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QGradient, QLinearGradient, QPen, QBrush
from PySide6.QtCore import QPoint, QRect, QRectF, QTimer, Qt
from ui_design2 import Ui_MainWindow  # Это наш конвертированный файл дизайна

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    resized = QtCore.Signal()
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self._translate = QtCore.QCoreApplication.translate
        self.topScene = QtWidgets.QGraphicsScene()
        self.topGraphicsView.setScene(self.topScene)

        self.connectSignals()

        timer = QTimer(self)
        timer.timeout.connect(self.drawTopScene)
        timer.start(100)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainApp, self).resizeEvent(event)

    def setStatus(self) -> None:
        msg = "Base: " + str(self.centralwidget.width()) + " : " + str(self.centralwidget.height())
        msg += ", Top: " + str(self.topGraphicsView.width()) + " : " + str(self.topGraphicsView.height())
        self.statusbar.showMessage(msg)

    def onResize(self) -> None:
        self.drawTopScene()
        self.setStatus()

    def connectSignals(self):
        # Connect your signals here like:
        # self.connectButton.clicked.connect(self.onPortConnect)
        self.resized.connect(self.onResize)

    def drawTopScene(self) -> None:
        self.topScene.clear()
        width = int(self.topGraphicsView.width() * 0.98)
        height = int(self.topGraphicsView.height() * 0.98)
        self.topScene.setSceneRect(0, 0, width, height)
        stepSize = 5
        spacerSize = 10

        pen = QtGui.QPen(Qt.gray)
        pen.setCosmetic(True)  # ***

        lgrad = QLinearGradient(0.5 * width, 0, 0.5 * width, height)
        lgrad.setColorAt(0.2, Qt.red)
        lgrad.setColorAt(0.5, Qt.yellow)
        lgrad.setColorAt(1.0, Qt.green)

        rnd = QtCore.QRandomGenerator().global_()

        for x in range(0, width, stepSize + spacerSize):
            lineHeight = height - rnd.bounded(height)

            topLeft = QPoint(x, lineHeight)
            botRight = QPoint(x+stepSize, height)
            rect = QRectF(topLeft, botRight)
            item = QGraphicsRectItem(rect)
            item.setBrush(QBrush(lgrad))
            item.setPen(pen)
            # creating a blur effect
            blur_effect = QGraphicsBlurEffect()
            # setting blur radius
            blur_effect.setBlurRadius(2)
            item.setGraphicsEffect(blur_effect)
            #self.topScene.addRect(rect, pen, QBrush(lgrad))
            self.topScene.addItem(item)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp

    window.setWindowTitle("Play with Graphics")

    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
