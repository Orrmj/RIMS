import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView

# Run program
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_view = MainView()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
