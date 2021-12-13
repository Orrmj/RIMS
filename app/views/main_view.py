from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from .view_crossing_form import WindowCrossingForm

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
        self.Crossing_Inspection_Application = qtw.QPushButton("Crossing Inspection Application", clicked=self.onChange)
        self.Track_Inspection_Application = qtw.QPushButton("Track Inspection Application", clicked=self.onChange)
        self.Bridge_Inspection_Application = qtw.QPushButton("Bridge Inspection Application", clicked=self.onChange)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.Crossing_Inspection_Application)

    @qtc.pyqtSlot()
    def onChange(self):
        self.formwindow = WindowCrossingForm()
        #self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.submitted[str].connect(self.onSubmittedStr)
        self.formwindow.submitted[int, str].connect(self.onSubmittedIntStr)
        self.formwindow.show()

    @qtc.pyqtSlot(str)
    def onSubmittedStr(self, string):
        self.label.setText(string)

    @qtc.pyqtSlot(int, str)
    def onSubmittedIntStr(self, integer, string):
        text = f'The string {string} becomes the number {integer}'
        self.label.setText(text)

 