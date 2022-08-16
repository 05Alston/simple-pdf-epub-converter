from ast import main
from curses import window
from mimetypes import init
import sys

# import GUI file
from proto1 import *

# Main class
class MainWindow(QMainWindow):
    def __init__ (self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Show window
        self.show()


# Execute App
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())