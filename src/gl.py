#!/usr/bin/env python3 
# -*- coding: utf-8 -*-


# to do: main window layout is not defined properly
# custom layout consists actually from one element figure of matplotlib. 
# it does not fit properly

# This is just executable application, opening the Main Window glDesignMW
# https://www.tutorialspoint.com/pyqt/pyqt_multiple_document_interface.htm


# sensors especially DHT 22 are slow. It takes too much time and irregular to get values. 
# could be done using pthread to avoid waiting also for sensors 
# after wait of LoggingRate

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *   # import including QTimer
from PyQt4.QtCore import *

from glDesignMW import *
import datetime
import PyTango

import matplotlib.dates as mdates
import urllib  # module with classes request parse ... we use only request class



# ==================================================================================
# This funny block is apparently for conversion of strings in different encoding
# copied from design object

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# ==================================================================================
# First!!!! We inherit  Design Class, developed in Qt Designer

class MyGView(Ui_MainWindow):
    # and add or redefine its code (properties and methods):
    
    # Properties:

    MaximalDataAmount = 120

    datatxt = [] # this is text data property which will be used to get Data From device
    # Depending on use: update or initialization the text Data will be used in different ways    

   
    # Default initial Source and Data amount for visualization
    #DataSource1 =  "http://192.168.12.1/sqlwrapper.php?len="
    #DataSource1 =  "http://192.168.2.110/sqlwrapper.php?len="
    DataSource1 =  "http://192.168.10.2/sqlwrapper.php?len="
    DataSource =  DataSource1
    
    Description = "CO2-Ampel"
    DataAmount = MaximalDataAmount        


    
        
    
    #def __init__(self):
    # ###   self = Ui_MainWindow() # call constructor of parent
    # it must first call setupui, which has MainWindow argument not available here. leave it so now
    
    # ================================================================================================================
    # This must be called in main text to connect all events to proper methods etc
    
    # But do it only once!!!!!! !!! it must be actually overloaded constructor
    # where the constructor of parent is called and additional methods are called.
    
    def init(self):        
        self.pushButton.clicked.connect(self.HelpButton_clicked) # connect onclick event of button with according function
        self.submenuProvideFeedback.triggered.connect(self.actionProvideFeedback)     
        self.submenuAbout.triggered.connect(self.actionAbout)   # Define Submenu Action for actionAbout
        
        self.comboBox.currentIndexChanged.connect(self.WindowActionCombo) #
        #self.comboBox.currentIndexChanged.triggered(self.WindowActionCombo) #        
        self.InitialiseMatplotlib()        
        self.pushButtonControlCO2Ampel.clicked.connect(self.ControlCO2Ampel_clicked) # connect onclick event of button with according function
        self.pushButton_2.clicked.connect(self.ControlCO2Ampel_On) # connect onclick event of button with according function
        self.pushButton_3.clicked.connect(self.ControlCO2Ampel_Off) # connect onclick event of button with according function
        self.checkBoxHumidity.clicked.connect(self.RePlot)
        self.checkBoxTemperatur.clicked.connect(self.RePlot)
        
        self.spinBox.valueChanged.connect(self.ControlCO2Ampel_SetLight) # connect onclick event of button with according function
        
        
        
        self.tabWidget.currentChanged.connect(self.onTab) #changed!
        
        
        #ui.menuAbout.triggered.connect(actionProvide_feedback) 
        try:
            print("================================================")
            self.dev = PyTango.DeviceProxy("p11/test/CO2Ampel")
            print(self.dev.ping()) 
            print("================================================")
            print(self.dev.info()) 
        except:
            pass


    # ================================================================================================================


    # Function to get Data from Devices. 
    # It uses property  DataSource of the object
    # The property must be defined before first call of this function. 
    
    # this function uses also property DataAmount of the object.
    # it must be accordingly also defined before first use.
    
    # The Function will be used for initial initialization during start of application
    # or during change of source  e.g with DataAmount = 500
    # or for data update with e.g. DataAmount =1    
    
    def GetDataFromDevice(self):
        from sys import platform
        
          
        http_request = self.DataSource + str(self.DataAmount)
        #print(http_request) 
        
        if platform == "linux" or platform == "linux2":
            NetObject = urllib.urlopen(http_request)  # it works, but with modifications from system to system. .request was there before
        else:     
            NetObject = urllib.request.urlopen(http_request)  # it works, but with modifications from system to system. .request was there before
        
        while len(self.datatxt) > 0 : self.datatxt.pop() # clean list
             
        self.datatxt = NetObject.read().decode('utf-8')
        #print(datatxt)
        self.datatxt = self.datatxt.split('\r\n') # UNTERCHIED MIT UNSERE FORMAT "Wagenrücklaufe"
        self.datatxt.pop()  ## remove last element of list since it is just empty element
    
        tlength = len(self.datatxt)
        for i in range(0,tlength):
            self.datatxt[i] = self.datatxt[i].replace('\t',' ')  # replace Tab by space
        
    def ExtractData(self):

        DateM = [row.split(' ')[0] for row in self.datatxt]
        TimeM  =  [row.split(' ')[1] for row in self.datatxt]
        RH  =  [row.split(' ')[2] for row in self.datatxt]        
        T  =  [row.split(' ')[3] for row in self.datatxt]
        CO2  =  [row.split(' ')[4] for row in self.datatxt]
        tlength = len(self.datatxt)
        #print(tlength)
        
        if (self.DataAmount>1):
            # initial                
            self.CO2 = []
            self.x = []
            self.T = []
            self.RH = []
            for i in range(tlength):
                dd = datetime.datetime.strptime(DateM[i] + ' ' + TimeM[i], '%d.%m.%Y %H:%M:%S')
                self.x.append(dd)    
                self.CO2.append(CO2[i])
                self.RH.append(RH[i])
                self.T.append(T[i])
            #print(self.CO2)
            #print(self.x)
            
            
        else:

            
            for i in range(tlength):                
                dd = datetime.datetime.strptime(DateM[i] + ' ' + TimeM[i], '%d.%m.%Y %H:%M:%S')
                if (dd!=self.x[0]): # do it only if new measurement is read
                
                    # REMOVE last element of list (earliest time) RECORD FROM self.CO2 and self.x append without clean:
                    if (len(self.x)>self.MaximalDataAmount): # just after restart of device the data sequence is short 
                        
                        # first the data will be expanded and they will be poped 
                        # if needed range is reached
                        self.CO2.pop(-1) 
                        
                        self.x.pop(-1)
                        self.RH.pop(-1)
                        self.T.pop(-1)
                
                
                    # insert in the beginning
                    self.x = [dd] + self.x     
                    self.CO2 = [CO2[i]] + self.CO2   
                    self.RH = [RH[i]] + self.RH
                    self.T = [T[i]] + self.T
                
                
    
    #return xUni, ADataUni[1], ADataUni[4] 

    def UpdateDataFromDevice(self):
        ## 
        self.DataAmount = 1 # to get just last record
        self.GetDataFromDevice() 
        self.ExtractData()


        
       # self.CO2.append(CO2Value)
        #self.x.append(dd)    
        
            
    def UpdateAndPlot(self):
        self.UpdateDataFromDevice()
        self.plot()
    
    

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
        
        
        self.GetDataFromDevice()  # actually it should be one function for first initialisation
        self.ExtractData()
        self.plot()
    
    def RePlot(self): # get argument - id of chosen room as it is in Combobox
        self.DataAmount=self.MaximalDataAmount
        self.plot()    
    
    
    def plot(self): # get argument - id of chosen room as it is in Combobox
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
        

        self.InfoLabel.setText(_translate("MainWindow", self.Description, None))       

        if (self.DataAmount>1): # First initialisation:
            self.SetFrame()
            
            line1 = self.ax1r.plot(self.x, self.CO2, '.', color='#00FF00', label=self.legends[2])
            self.lns = line1
            
            if (self.checkBoxTemperatur.checkState()):
                line2 = self.ax.plot(self.x, self.T, '.', color='#FF0000', label=self.legends[0])
                self.lns =  self.lns + line2
            if (self.checkBoxHumidity.checkState()):      
                line3 = self.ax.plot(self.x, self.RH, '.', color='#0000FF', label=self.legends[1])
                self.lns =  self.lns + line3
            
        else:
            self.SetFrame()
            if (self.checkBoxTemperatur.checkState()):
                self.ax.plot(self.x, self.T, '.', color='#FF0000', label=self.legends[0])
            if (self.checkBoxHumidity.checkState()):    
                self.ax.plot(self.x, self.RH, '.', color='#0000FF', label=self.legends[1])
                
            self.ax1r.plot(self.x, self.CO2, '.', color='#00FF00', label=self.legends[2])
            
        self.SetFrameAfterPlot()
            
            
            
                
        
        # refresh canvas
        self.canvas.draw()
        
    def SetFrame(self):
        # do it only once      
        self.myFmt = mdates.DateFormatter('%H:%M')   # '%d.%m.%Y %H:%M'        
        self.legends = ['Temperatur', 'relative Feuchtigkeit', 'CO2-Konzentration']
        # create an axis
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()  # discards the old graph        
        self.ax.set_ylabel(u'T, °C, oder RH, %') # 
        self.ax1r = self.ax.twinx()    
        self.ax1r.clear()  # discards the old graph 
        self.ax1r.set_ylabel('CO2, ppm')
        self.ax1r.set_ylim([300, 3000])
        leftmargin= 0.13
        h = 0.94
        shift = 0.03
        s = "Start Date and Time: "  + self.x[-1].strftime("%d.%m.%Y %H:%M")
        self.figure.text(leftmargin, h, s)
        h = h - shift           
        self.figure.text(leftmargin, h, "Description: " + self.Description + '.')
        #self.figure.autofmt_xdate()
        self.ax.xaxis.set_major_formatter(self.myFmt)
        self.ax.set_ylim([0, 105])        
        
        # info about figure
        #title = "Luftqualitaet"
        
        #ax.set_title(title)
        self.ax.set_xlabel('t')

    def SetFrameAfterPlot(self):        
        self.labs = [l.get_label() for l in self.lns]
        self.figure.legend(self.lns, self.labs, loc='upper center', ncol=3, prop={'size':10},  markerscale=2) #   , bbox_to_anchor=(0.5, -0.2)        


    # ============================================================================================================
    # Menu Actions

    def actionProvideFeedback(self):
        #This function is just to train menu points       
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Just simple at the moment. email: p.v.paulau@gmail.com")    
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel #function displays desired buttons.
        msg.exec_()


    def actionAbout(self):
        #This function just shows About Info. 
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("gl - Gute Luft Software. To view the data of airquality Sensors. To Control Device via Tango. 2018. DESY, Jade Hochschule.")    
        msg.setWindowTitle("About guteluftGUI")
        msg.setStandardButtons(QMessageBox.Ok) #  | QMessageBox.Cancel #function displays desired buttons.
        msg.exec_()

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
        self.InfoLabel.setText(_translate("MainWindow", smsg, None))       
        
        self.DataSource =  self.DataSource1 #"http://192.168.12.1/sqlwrapper.php?len=" # must be adjusted here for each room
        self.Description = self.comboBox.itemText(i)
        self.DataAmount = self.MaximalDataAmount        
        
        self.GetDataFromDevice()  # actually it should be one function for first initialisation
        self.ExtractData()
        self.plot()

    # Override resize event
    def resizeEvent(self, event):
        print("resize")

    def ControlCO2Ampel_clicked(self):
        try:
            self.dev.StartTest()
        except:
            pass
        
    def ControlCO2Ampel_On(self):
        try:
            self.dev.SwitchOn()
        except:
            print("No device server available")
            pass

    def ControlCO2Ampel_Off(self):
        try:
            self.dev.SwitchOff()
        except:
            print("No device server available")
            pass
        
        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 300, 591))
        
        #self.verticalLayoutWidget = QtGui.QWidget(self.TabCO2Ampel)
        #self.layout.
        
    def ControlCO2Ampel_SetLight(self):
        try:
            ###self.InfoLabel.setText(self.spinBox.value())
            print(self.spinBox.value())
            self.dev.SetLight(self.spinBox.value())
        except:
            print("No device server available")
            pass

        
    
    
    
    def onTab(self):
        ci = self.tabWidget.currentIndex()
        if (ci == 0):                        
            self.DataSource =  self.DataSource1
            self.Description = "Jade-Hochschule"
            self.DataAmount = self.MaximalDataAmount
            
            self.WindowActionCombo()        
            
        if (ci == 1):
            self.DataSource =  self.DataSource1            
            self.Description = "CO2-Ampel"
            self.DataAmount = self.MaximalDataAmount        
    
    #tabGuteLuft 
            

# ============================================================================================================
# Main code:


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()


    ui = MyGView()
    ui.setupUi(MainWindow)
    ui.init()

    timer = QTimer()

    # it should be one function for initial Get Data and another function for update, 
    # since one record must be added and one record must be deleted and not just reread    
        
    timer.timeout.connect(ui.UpdateAndPlot)
    timer.start(1000)


 
    MainWindow.show()
    sys.exit(app.exec_())

