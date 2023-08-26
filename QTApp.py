import sys

# 3rd party imports
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

# Local imports
from main_qobject import Main


def main():
    # noinspection PyTypeChecker
    QApplication.setAttribute(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    # Create instance of main QObject and appinfo
    instance = Main()

    # Start showing the main window and make it the focus
    instance.main_window.show()
    instance.main_window.activateWindow()

    # Execute and close program on exit
    sys.exit(instance.app.exec())


if __name__ == "__main__":
    main()