from jarvisgui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import main
import sys
import datetime

class MainThread(QThread):


    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        main.executer()
StartExe = MainThread()

class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.triggerjarvis.clicked.connect(self.startTask)
        self.gui.shutengine.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("GUI images//system initialising.gif")
        self.gui.initialising.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("GUI images//background.gif")
        self.gui.backgroud.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("GUI images//tumblr_nrqm32yH3W1r6xm5co1_640.gif")
        self.gui.voice.setMovie(self.gui.label3)
        self.gui.label3.start()

        #timer = QTimer(self)
        #timer.timeout.connect(self)
        #tmer.start(999)

        #crt = QTime.currentTime()
        #crdt = QDate.currentDate()
        #time = crt.toString('hh:mm:ss')
        #date = crdt.toString()
        #self.gui.datetime.setText(date+"  "+time)

        tnow = datetime.datetime.now().strftime('%H:%M:%S')  #this shows entry log time
        self.gui.datetime.setText(tnow)                      #this shows entry log time

        self.gui.jarvisstatus.setText("ONLINE")
        self.gui.databasestatus.setText("OFFLINE")
        self.gui.temp.setText("27°C")
        if main.database_variable == 1 :
            self.gui.databasestatus.setText("ONLINE")

        StartExe.start()

    def database(self):
        self.gui.databasestatus.setText("ONLINE")

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
