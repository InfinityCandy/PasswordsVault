import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

from mainScreen import MainScreen

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainScreen = MainScreen()

    sys.exit(app.exec_())