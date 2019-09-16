import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

import mainScreen

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainScr = mainScreen.MainScreen()

    sys.exit(app.exec_())