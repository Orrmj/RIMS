import sys
import datetime
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from views.view_ui_crossing_form import UI_CrossingForm

class WindowCrossingForm(qtw.QWidget):

    submitted = qtc.pyqtSignal([str], [int, str])

    #settings = {'show_warnings': True}
    settings = qtc.QSettings('Alan D Moore', 'text editor')

    def __init__(self):
        super().__init__()

        self._ui = UI_CrossingForm()
