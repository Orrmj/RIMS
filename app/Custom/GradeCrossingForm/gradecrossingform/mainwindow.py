from PyQt5 import QtWidgets as qtw
#from PyQt5 import QtGui as qtg
#from PyQt5 import QtCore as qtc

from gradecrossingform.controllers.controller_crossing_assessment_ca import ControllerCrossingAssessmentCA

class MainWindow(qtw.QWidget):

    def __init__(self):
        '''MainWindow constructor'''
        super().__init__() # create default constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window and display its contents to the screen. 
        """
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Grade Crossing Application')
        self.displayWidgetsToCollectInfo()
        self.show()

    def displayWidgetsToCollectInfo(self):
        """
        Create widgets that will be used to collect information
        from the user to create a new account. 
        """
        self.setLayout(qtw.QVBoxLayout())
        self.label = qtw.QLabel('Click "change" to change this text.')
        self.Crossing_Inspection_Application = qtw.QPushButton("Crossing Inspection Application", clicked=self.FormCrossingCA)
        #self.Track_Inspection_Application = qtw.QPushButton("Track Inspection Application", clicked=self.onChange)
        #self.Bridge_Inspection_Application = qtw.QPushButton("Bridge Inspection Application", clicked=self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.Crossing_Inspection_Application)

    def FormCrossingCA(self):
        self.formWindow = ControllerCrossingAssessmentCA()