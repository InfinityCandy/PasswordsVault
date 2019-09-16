import sys
from mainScreen import mainScreen
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

#Window Size
windowWidth = 400
windowHeigh = 150

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    ex = mainScreen(windowWidth, windowHeigh)
    sys.exit(app.exec_())