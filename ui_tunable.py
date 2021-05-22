# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design3.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 288)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.barWidth = QDial(self.centralwidget)
        self.barWidth.setObjectName(u"barWidth")
        self.barWidth.setMinimum(1)
        self.barWidth.setMaximum(40)
        self.barWidth.setValue(10)
        self.barWidth.setNotchesVisible(True)

        self.gridLayout_2.addWidget(self.barWidth, 2, 2, 1, 1)

        self.barSpacing = QDial(self.centralwidget)
        self.barSpacing.setObjectName(u"barSpacing")
        self.barSpacing.setMaximum(40)
        self.barSpacing.setValue(2)
        self.barSpacing.setNotchesVisible(True)
        self.barSpacing.setTracking(False)

        self.gridLayout_2.addWidget(self.barSpacing, 2, 3, 1, 1)

        self.labelGr = QLabel(self.centralwidget)
        self.labelGr.setObjectName(u"labelGr")
        self.labelGr.setTextFormat(Qt.PlainText)
        self.labelGr.setScaledContents(False)
        self.labelGr.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.labelGr, 1, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_3, 1, 4, 1, 1)

        self.yellowLvl = QDial(self.centralwidget)
        self.yellowLvl.setObjectName(u"yellowLvl")
        self.yellowLvl.setMaximum(10)
        self.yellowLvl.setValue(2)
        self.yellowLvl.setWrapping(False)
        self.yellowLvl.setNotchesVisible(True)
        self.yellowLvl.setTracking(False)

        self.gridLayout_2.addWidget(self.yellowLvl, 0, 3, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_2, 1, 3, 1, 1)

        self.greenLvl = QDial(self.centralwidget)
        self.greenLvl.setObjectName(u"greenLvl")
        self.greenLvl.setMaximum(10)
        self.greenLvl.setSingleStep(1)
        self.greenLvl.setValue(7)
        self.greenLvl.setTracking(False)
        self.greenLvl.setOrientation(Qt.Horizontal)
        self.greenLvl.setInvertedAppearance(False)
        self.greenLvl.setInvertedControls(False)
        self.greenLvl.setNotchesVisible(True)

        self.gridLayout_2.addWidget(self.greenLvl, 0, 1, 1, 2)

        self.refreshSpeed = QDial(self.centralwidget)
        self.refreshSpeed.setObjectName(u"refreshSpeed")
        self.refreshSpeed.setMinimum(50)
        self.refreshSpeed.setMaximum(1000)
        self.refreshSpeed.setSingleStep(50)
        self.refreshSpeed.setPageStep(100)
        self.refreshSpeed.setValue(200)
        self.refreshSpeed.setSliderPosition(200)
        self.refreshSpeed.setInvertedAppearance(True)
        self.refreshSpeed.setInvertedControls(False)
        self.refreshSpeed.setNotchesVisible(True)
        self.refreshSpeed.setTracking(False)

        self.gridLayout_2.addWidget(self.refreshSpeed, 2, 4, 1, 1)

        self.redLvl = QDial(self.centralwidget)
        self.redLvl.setObjectName(u"redLvl")
        self.redLvl.setMaximum(10)
        self.redLvl.setValue(1)
        self.redLvl.setSingleStep(1)
        self.redLvl.setNotchesVisible(True)
        self.redLvl.setTracking(False)

        self.gridLayout_2.addWidget(self.redLvl, 0, 4, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_4, 3, 2, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 4, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label_6, 3, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelGr.setText(QCoreApplication.translate("MainWindow", u"Green lvl", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Red lvl", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Yellow lvl", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Spacing", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
    # retranslateUi

