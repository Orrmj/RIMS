import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import csv

class CsvTableModel(qtc.QAbstractTableModel):
    """The model for a CSV table."""

    def __init__(self, csv_file):
        super().__init__()

        self.tableview = qtw.QTableView()
        self.tableview.setSortingEnabled(True)
        self.setCentralWidget(self.tableview)

        # Setup the menu
        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        file_menu.addAction('Open', self.select_file)
        file_menu.addAction('Save', self.save_file)

        edit_menu = menu.addMenu('Edit')
        edit_menu.addAction('Insert Above', self.insert_above)
        edit_menu.addAction('Insert Below', self.insert_below)
        edit_menu.addAction('Remove Row(s)', self.remove_rows)
        
        self.filename = csv_file
        with open(self.filename) as fh:
            csvreader = csv.reader(fh)
            self._headers = next(csvreader)
            self._data = list(csvreader)

        
    # File methods
    def select_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            'Select a CSV file to open…',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        if filename:
            self.model = CsvTableModel(filename)
            self.tableview.setModel(self.model)

    def save_file(self):
        if self.model:
            self.model.save_data()

    # Methods for insert/remove

    def insert_above(self):
        selected = self.tableview.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    def insert_below(self):
        selected = self.tableview.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def remove_rows(self):
        selected = self.tableview.selectedIndexes()
        # Errata:  The book contains the following code:
        #if selected:
        #    self.model.removeRows(selected[0].row(), len(selected), None)

        # This is incorrect, as len(selected) is the number of *cells* selected,
        # not the number of *rows* selected.

        # correct approach would look like this:
        num_rows = len(set(index.row() for index in selected))
        if selected:
            self.model.removeRows(selected[0].row(), num_rows, None)


class MainWindow(qtw.QMainWindow):

    model = None

    def __init__(self):
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here

        self.tableview = qtw.QTableView()
        self.tableview.setSortingEnabled(True)
        self.setCentralWidget(self.tableview)

        # Setup the menu       menu = self.menuBar()
        file_menu = menu.addMenu('File')
        file_menu.addAction('Open', self.select_file)
        file_menu.addAction('Save', self.save_file)

        edit_menu = menu.addMenu('Edit')
        edit_menu.addAction('Insert Above', self.insert_above)
        edit_menu.addAction('Insert Below', self.insert_below)
        edit_menu.addAction('Remove Row(s)', self.remove_rows)

        # End main UI code
        self.show()

    # File methods
    def select_file(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            'Select a CSV file to open…',
            qtc.QDir.homePath(),
            'CSV Files (*.csv) ;; All Files (*)'
        )
        if filename:
            self.model = CsvTableModel(filename)
            self.tableview.setModel(self.model)

    def save_file(self):
        if self.model:
            self.model.save_data()

    # Methods for insert/remove

    def insert_above(self):
        selected = self.tableview.selectedIndexes()
        row = selected[0].row() if selected else 0
        self.model.insertRows(row, 1, None)

    def insert_below(self):
        selected = self.tableview.selectedIndexes()
        row = selected[-1].row() if selected else self.model.rowCount(None)
        self.model.insertRows(row + 1, 1, None)

    def remove_rows(self):
        selected = self.tableview.selectedIndexes()
        # Errata:  The book contains the following code:
        #if selected:
        #    self.model.removeRows(selected[0].row(), len(selected), None)

        # This is incorrect, as len(selected) is the number of *cells* selected,
        # not the number of *rows* selected.

        # correct approach would look like this:
        num_rows = len(set(index.row() for index in selected))
        if selected:
            self.model.removeRows(selected[0].row(), num_rows, None)