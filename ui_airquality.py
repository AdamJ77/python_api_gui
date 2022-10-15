# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'airquality.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 373)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.stations = QListWidget(self.splitter)
        self.stations.setObjectName(u"stations")
        self.splitter.addWidget(self.stations)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stack = QLabel(self.page)
        self.stack.setObjectName(u"stack")
        self.stack.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.stack)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stationName = QLabel(self.page_2)
        self.stationName.setObjectName(u"stationName")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stationName.setFont(font)
        self.stationName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.stationName)

        self.sensors = QListWidget(self.page_2)
        self.sensors.setObjectName(u"sensors")

        self.verticalLayout_3.addWidget(self.sensors)

        self.plot = QLabel(self.page_2)
        self.plot.setObjectName(u"plot")
        self.plot.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.plot)

        self.verticalSpacer = QSpacerItem(20, 271, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_2)
        self.splitter.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 467, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Air Quality", None))
        self.stack.setText(QCoreApplication.translate("MainWindow", u"Choose station first", None))
        self.stationName.setText("")
        self.plot.setText("")
    # retranslateUi

