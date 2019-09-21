from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox, QPlainTextEdit

class ShowPasswordInfo(QMainWindow):
    def __init__(self, passwordInfo):
        super().__init__()

        #Attributes
        self.windowWidth = 300
        self.windowHeigh = 100
        self.passwordInfo = passwordInfo

        #This method is executed when the class's object is created
        self.drawWindow()

    def drawWindow(self): 
        passwordInfoArea = QPlainTextEdit(self)
        passwordInfoArea.setPlainText(self.formatPasswordInfo(self.passwordInfo))
        passwordInfoArea.resize(250, 60)
        passwordInfoArea.move(20, 20)

        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle("Password Information")    
        self.show()

    def formatPasswordInfo(self, passwordInfoUnformatted):
        passwordInfoFormatted = passwordInfoUnformatted.replace("-", "\n")
        passwordInfoFormatted = passwordInfoFormatted.replace(":", ": ")

        return passwordInfoFormatted