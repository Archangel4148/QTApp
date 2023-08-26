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

        #Set the background theme color to purple
        self.setStyleSheet("background-color: purple;")

        #Triggers for functions based on button(s) clicked
        self.ui.pushButton.clicked.connect(self.plusOne)
        self.ui.pushButton_2.clicked.connect(self.minusOne)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.submitButton.clicked.connect(self.setValue)

    #Add 1 to the label value when the "+1" button is clicked
    def plusOne(self):
        self.ui.label.setText(str(int(self.ui.label.text()) + 1))

    #Subtract 1 from the label value when the "-1" button is clicked
    def minusOne(self):
        self.ui.label.setText(str(int(self.ui.label.text()) - 1))

    #Reset the label value to "0" when the Reset button is clicked
    def reset(self):
        self.ui.label.setText("0")

    def setValue(self):
        value = self.ui.textInput.text()
        if value == '':
            self.ui.label.setText("ERROR, no input")
        elif not value.isnumeric():
            self.ui.label.setText("ERROR, invalid value")
        else:
            self.ui.label.setText(str(self.ui.textInput.text()))

