import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import QGradient, QLinearGradient, QPen, QBrush
from PySide6.QtCore import QPoint, QRect, QRectF, QTimer, Qt
from ui_tunable import Ui_MainWindow  # Это наш конвертированный файл дизайна

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    resized = QtCore.Signal()
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self._translate = QtCore.QCoreApplication.translate
        self.topScene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.topScene)

        self.connectSignals()

        self.statusUpdated = 1

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawTopScene)
        self.timer.start(self.refreshSpeed.value())

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainApp, self).resizeEvent(event)

    def setStatus(self) -> None:
        msg = "[Bar width]: " + str(self.barWidth.value()) + " [Bar Spacing]: " + str(self.barSpacing.value())
        msg += " [Refresh]: " + str(self.refreshSpeed.value()) + "ms"
        self.statusbar.showMessage(msg)
        self.statusUpdated = 0 # No new data to show in status

    def onResize(self) -> None:
        self.drawTopScene()

    def onRefreshSpeedChange(self) -> None:
        self.timer.stop()
        self.timer.start(self.refreshSpeed.value())
        self.statusUpdated = 1

    def onBarWidthChange(self) -> None:
        self.statusUpdated = 1

    def onBarSpacingChange(self) -> None:
        self.statusUpdated = 1

    def getGreenLvl(self) -> float:
        return self.greenLvl.value() / 10

    def getYellowLvl(self) -> float:
        return self.yellowLvl.value() / 10

    def getRedLvl(self) -> float:
        return self.redLvl.value() / 10

    def connectSignals(self):
        # Connect your signals here like:
        # self.connectButton.clicked.connect(self.onPortConnect)
        self.resized.connect(self.onResize)
        self.refreshSpeed.valueChanged.connect(self.onRefreshSpeedChange)
        self.barWidth.valueChanged.connect(self.onBarWidthChange)
        self.barSpacing.valueChanged.connect(self.onBarSpacingChange)

    def drawTopScene(self) -> None:
        self.topScene.clear()
        width = int(self.graphicsView.width() * 0.98)
        height = int(self.graphicsView.height() * 0.98)
        self.topScene.setSceneRect(0, 0, width, height)
        stepSize = self.barWidth.value()
        spacerSize = self.barSpacing.value()

        pen = QtGui.QPen(Qt.gray)
        pen.setCosmetic(True)  # ***

        lgrad = QLinearGradient(0.5 * width, 0, 0.5 * width, height)
        lgrad.setColorAt(self.getRedLvl(), Qt.red)
        lgrad.setColorAt(self.getYellowLvl(), Qt.yellow)
        lgrad.setColorAt(self.getGreenLvl(), Qt.green)

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
            blur_effect.setBlurRadius(1.5)
            item.setGraphicsEffect(blur_effect)
            #self.topScene.addRect(rect, pen, QBrush(lgrad))
            self.topScene.addItem(item)

        if self.statusUpdated:
            self.setStatus()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainApp()  # Создаём объект класса ExampleApp

    window.setWindowTitle("Play with Graphics")

    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
