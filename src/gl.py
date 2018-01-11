#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# This is just executable application, opening the Main Window glDesignMW
# https://www.tutorialspoint.com/pyqt/pyqt_multiple_document_interface.htm

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from glDesignMW import *


# ==================================================================================
# This funny block is apparently for conversion of stricngs in different encoding
# copied from design object

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# ==================================================================================
# First!!!! We inherite Design Class, developed in Qt Designer

class MyGView(Ui_MainWindow):
    # and define or redefine its code :
    
    #def __init__(self):
    # ###   self = Ui_MainWindow() # call constructor of parent
    # it must first call setupui, which has MainWindow argument not available here. leave it so now
    
    # ================================================================================================================
    # This must be called in main text to connect all events to proper methods etc
    
    # But do it only once!!!!!! !!! it must be actually overloaded constructor
    # where the constructor of parent is called and additional methods are called.
    
    def init(self):        
        self.pushButton.clicked.connect(self.HelpButton_clicked) # connect onclick event of button with according function
        self.actionProvide_feedback.triggered.connect(self.actionProvide_feedback1)     
        self.actionAbout.triggered.connect(self.actionAbout1)   # Define Submenu Action for actionAbout
        self.actionSave_Image.triggered.connect(self.WindowActionTest) #
        self.comboBox.currentIndexChanged.connect(self.WindowActionCombo) #
        #self.comboBox.currentIndexChanged.triggered(self.WindowActionCombo) #
        
        self.InitialiseMatplotlib()
        
        self.pushButtonControlCO2Ampel.clicked.connect(self.ControlCO2Ampel_clicked) # connect onclick event of button with according function
        
        
        
        
        

    #ui.menuAbout.triggered.connect(actionProvide_feedback) 
    # ================================================================================================================
    
    
    def WindowActionTest(self):
        print ("Window Action Test")

    # ============================================================================================================
    # Actions to handle Matplotlib things:

    def InitialiseMatplotlib(self):   
        from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
        from matplotlib.figure import Figure

        #import random

        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.toolbar = NavigationToolbar("xx", self.canvas) #

        #set the layout

        #self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        #self.layout.addWidget(self.button)
        #self.setLayout(layout)        
        
        self.WindowActionCombo() # activates default Room 

    
    def plot(self,room_id): # get argument - id of chosen room as it is in Combobox
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # The meaning and essence of this application is actually in Visualization of Data from remote computers
        # therefore the data must be necessarily taken from some network computer. 
        # We assume, they are available via http. (e.g. php wrapper which provides last n values in the databasetable)
        
        # The essence of this application is also to visualise live data with possibly fast rate. 
        # To do it, one needs to start additional "Fast" logger, which will save all data in RHTCO2fast table. 
        # It must not save files. It must clean table at start. Server part and "client" - to be done here at home   
        
        # To implement it, one needs to remake RHTCO2 logger in OOP style. 
        # all loggers do the same. creation(Initialization), infinite loop, reed sensor(s) save Data, and wait, and Destroy 
        # hence we create abstract class Logger and short main file.
        # we implement then Class RHTCO2, which will inherit Logger and we implement methods Init, ReadSensors, 
        # SaveData, Wait(), Cleanup
        # 
        # One more option will be added - bool FastMonittoring. If it is True, then we do not save data in usual way but 
        # Save only in FAST table (cleaning it, is size is more than FastTableMaxSize - additional parameter)
        # we must create php wrapper, which simply gets returns all table or only last element of a table.
        
        # The scripts must be published on guteluft.jade-hs.de WebPage in new section "downloads". 
        
        # The guteluftGUI must be also published on guteluft webpage
        
        # define property of the  MyGView class which will contain a list of records for all rooms to monitor.
        
        # This software has options to work with A) local  device - CO2-Ampel B) with gutelugt.jade-HS.de
        # accordingly, a toolbar must be defined.  
        
              
                
        
        
        data = [j*room_id for j in range(10)]

        # create an axis
        ax = self.figure.add_subplot(111)        
        ax.clear()  # discards the old graph

        # plot data
        ax.plot(data, '*-')
        
        # info about figure
        title = self.comboBox.itemText(room_id)
        ax.set_title(title)
        ax.set_xlabel('t')



        # refresh canvas
        self.canvas.draw()
        



    # ============================================================================================================
    # Menu Actions

    def actionProvide_feedback1(self):
        #This function will be implemented later
       
        print ("Help Button clicked")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("It will be implemented later.")    
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel #function displays desired buttons.
        retval = msg.exec_()

    def actionAbout1(self):
        #This function just shows About Info. 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("gl - Gute Luft Software. To view the data of airquality Sensors. 2018. Jade Hochschule.")    
        msg.setWindowTitle("About guteluft.jade-hs.de")
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel #function displays desired buttons.
        retval = msg.exec_()

    def actionAboutOne(self):
        #This function just shows About Info. 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("gl - Gute Luft Software. To view the data of airquality Sensors. 2018. Jade Hochschule.")    
        msg.setWindowTitle("About guteluft.jade-hs.de")
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel #function displays desired buttons.
        retval = msg.exec_()



    # ============================================================================================================
    # Actions of Buttons ComboBox and other elements of the Window.

    def HelpButton_clicked(self):
        #print "Help Button clicked"
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This program is created to visualise the data of airquality from the network of sensors of Jade Hochschule. The sensors are installed in different buildings in different rooms in Oldenburg(De). The room like H-I-21 means: H-Hauptgebäude, I-erste Obergeschoss(second floor), 21 - roomnumber. For detailed description of buildings, see Lageplan in guteluft.jade-hs.de")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Help Message")
        #msg.setDetailedText("The details are as follows:")

        #function displays desired buttons.
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel

        #msg.buttonClicked.connect(msgbtn)
        retval = msg.exec_()
        #print "value of pressed message box button:", retval

    def WindowActionCombo(self):

        i = self.comboBox.currentIndex();
        smsg = self.comboBox.itemText(i)
        self.TestLabel.setText(_translate("MainWindow", smsg, None)) 
               
        self.plot(i)

    def ControlCO2Ampel_clicked(self):
        print("sdsd")
        #self.verticalLayoutWidget = QtGui.QWidget(self.TabCO2Ampel)
        #self.layout.

# ============================================================================================================
# Main code:


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()


    ui = MyGView()
    ui.setupUi(MainWindow)
    ui.init()


 
    MainWindow.show()
    sys.exit(app.exec_())

