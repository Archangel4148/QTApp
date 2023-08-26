# 3rd party imports
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

import sys

# Local imports
from main_window import MainWindow


class Main(QObject):
    """Main QObject for program which contains all following windows and devices.

    Initializes Qt and pyqtgraph for how they will be used for the rest of the program. This also creates an
    instance of the devices class which will be used to reference connected devices.
    There is the possibility that the devices class may become an inherited class and then there may be a camera class
    vhs class etc.

    Typical usage example:
        instance = Main()
        instance.main_window.show()
        instance.main_window.activateWindow()
    """

    def __init__(self):
        super().__init__()

        # Initialize Qt Sys
        self.app = QApplication(sys.argv)
        self.app.setStyle("fusion")

        # Set icon
        # icon = QIcon("icon.ico")
        # self.app.setWindowIcon(icon)

        # Initialize all objects
        self.main_window = MainWindow()

        # Set title for window
        self.main_window.setWindowTitle("My App")
        self.main_window.setWindowIcon(QIcon("./main_window/images/trollface.png"))
        self.main_window.destroyed.connect(self.close)


    def close(self):
        # Restore output streams
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        # Quit program
        self.app.quit()