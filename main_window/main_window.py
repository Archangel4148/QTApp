from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from main_window.main_window_init import Ui_MainWindow


class MainWindow(QMainWindow):
    """QMainWindow object that contains all the ui elements for the main window.

    This handles the graph object, table, and other items.
    """

    def __init__(self):
        super().__init__()

        # Initialize Ui and attributes
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.showMaximized()