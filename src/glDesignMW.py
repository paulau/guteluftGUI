# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glDesignMW.ui'
#
# Created: Mon Feb 12 23:55:30 2018
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1247, 850)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1451, 141))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabGuteLuft = QtGui.QWidget()
        self.tabGuteLuft.setObjectName(_fromUtf8("tabGuteLuft"))
        self.label = QtGui.QLabel(self.tabGuteLuft)
        self.label.setGeometry(QtCore.QRect(10, 10, 391, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tabGuteLuft)
        self.label_2.setGeometry(QtCore.QRect(10, 42, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.tabGuteLuft)
        self.comboBox.setGeometry(QtCore.QRect(10, 62, 191, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.tabGuteLuft)
        self.pushButton.setGeometry(QtCore.QRect(360, 10, 100, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tabGuteLuft, _fromUtf8(""))
        self.TabCO2Ampel = QtGui.QWidget()
        self.TabCO2Ampel.setObjectName(_fromUtf8("TabCO2Ampel"))
        self.label_4 = QtGui.QLabel(self.TabCO2Ampel)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 391, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.TabCO2Ampel)
        self.label_6.setGeometry(QtCore.QRect(360, 0, 421, 71))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButtonControlCO2Ampel = QtGui.QPushButton(self.TabCO2Ampel)
        self.pushButtonControlCO2Ampel.setGeometry(QtCore.QRect(360, 70, 141, 27))
        self.pushButtonControlCO2Ampel.setObjectName(_fromUtf8("pushButtonControlCO2Ampel"))
        self.pushButton_2 = QtGui.QPushButton(self.TabCO2Ampel)
        self.pushButton_2.setGeometry(QtCore.QRect(509, 70, 75, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.TabCO2Ampel)
        self.pushButton_3.setGeometry(QtCore.QRect(592, 70, 83, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.spinBox = QtGui.QSpinBox(self.TabCO2Ampel)
        self.spinBox.setGeometry(QtCore.QRect(710, 70, 54, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.tabWidget.addTab(self.TabCO2Ampel, _fromUtf8(""))
        self.checkBoxTemperatur = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxTemperatur.setGeometry(QtCore.QRect(40, 160, 131, 23))
        self.checkBoxTemperatur.setChecked(True)
        self.checkBoxTemperatur.setObjectName(_fromUtf8("checkBoxTemperatur"))
        self.checkBoxHumidity = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxHumidity.setGeometry(QtCore.QRect(40, 140, 101, 23))
        self.checkBoxHumidity.setChecked(True)
        self.checkBoxHumidity.setObjectName(_fromUtf8("checkBoxHumidity"))
        self.labelInfo = QtGui.QLabel(self.centralwidget)
        self.labelInfo.setGeometry(QtCore.QRect(40, 190, 291, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelInfo.setFont(font)
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 1211, 601))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(-1, -1, 0, -1)
        self.layout.setObjectName(_fromUtf8("layout"))
        self.InfoLabel = QtGui.QLabel(self.centralwidget)
        self.InfoLabel.setGeometry(QtCore.QRect(360, 190, 591, 16))
        self.InfoLabel.setText(_fromUtf8(""))
        self.InfoLabel.setObjectName(_fromUtf8("InfoLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1247, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMain = QtGui.QMenu(self.menubar)
        self.menuMain.setObjectName(_fromUtf8("menuMain"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.submenuProvideFeedback = QtGui.QAction(MainWindow)
        self.submenuProvideFeedback.setObjectName(_fromUtf8("submenuProvideFeedback"))
        self.submenuAbout = QtGui.QAction(MainWindow)
        self.submenuAbout.setObjectName(_fromUtf8("submenuAbout"))
        self.menuMain.addAction(self.submenuProvideFeedback)
        self.menuHelp.addAction(self.submenuAbout)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "guteluft.jade-hs.de", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "This section is to view a data of guteluft.jade-hs.de", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Chose the room:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "H-I-07", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "H-I-10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "H-I-21", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Get help!", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGuteLuft), QtGui.QApplication.translate("MainWindow", "guteluft.jade-hs.de", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "This section is to view a data of CO2-Ampel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"justify\">We will train here to control Device via Tango. For training aims, the MySQL Tango-Database(Tango Server) must be configured on some computer.  &quot;Tango Device Server&quot; - just Raspberry controlling LEDS. </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonControlCO2Ampel.setText(QtGui.QApplication.translate("MainWindow", "Test \"Tango Device\"", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "LED On", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "LED OFF", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TabCO2Ampel), QtGui.QApplication.translate("MainWindow", "CO2-Ampel", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxTemperatur.setText(QtGui.QApplication.translate("MainWindow", "Temperatur", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxHumidity.setText(QtGui.QApplication.translate("MainWindow", "Humidity", None, QtGui.QApplication.UnicodeUTF8))
        self.labelInfo.setText(QtGui.QApplication.translate("MainWindow", "Live visualisation of Data from device:", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMain.setTitle(QtGui.QApplication.translate("MainWindow", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.submenuProvideFeedback.setText(QtGui.QApplication.translate("MainWindow", "Provide feedback", None, QtGui.QApplication.UnicodeUTF8))
        self.submenuAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

