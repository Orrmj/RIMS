from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from .view_crossing_form import ViewCrossingForm
from models.model_crossing import ModelGradeCrossing

class MainView(qtw.QWidget):
    def __init__(self):
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
        self.Crossing_Inspection_Application = qtw.QPushButton("Crossing Inspection Application", clicked=self.GradeCrossingForm)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.Crossing_Inspection_Application)

    def GradeCrossingForm(self):
        self.model = ModelGradeCrossing()
        self.view = ViewCrossingForm(self.model)
        self.view.show()

 