from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox, QPlainTextEdit

import mainScreen

class ShowPasswordInfo(QMainWindow):
    def __init__(self, passwordInfo):
        super().__init__()

        #Attributes
        self.windowWidth = 300
        self.windowHeigh = 225
        self.passwordInfo = passwordInfo

        #This method is executed when the class's object is created
        self.drawWindow()

    def drawWindow(self): 
        passwordInfoArea = QPlainTextEdit(self)
        passwordInfoArea.setReadOnly(True)
        passwordInfoArea.setPlainText(self.formatPasswordsInfo(self.passwordInfo))
        passwordInfoArea.resize(250, 150)
        passwordInfoArea.move(20, 20)

        #Draws the button to go back
        backbtn = QPushButton("Go back to main menu", self)
        backbtn.clicked.connect(self.returnToMainScreen)
        backbtn.resize(250, 25)
        backbtn.move(20, 180)

        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle("Password Information")    
        self.show()

    def formatPasswordsInfo(self, passwordsInfoUnformatted):
        passwordsInfoFormatted = ""

        for passwordInfo in passwordsInfoUnformatted:
            passwordsInfoFormatted = passwordsInfoFormatted + ("-".join(passwordInfo)) + "\n\n"

        passwordsInfoFormatted = passwordsInfoFormatted.replace("-", "\n")
        passwordsInfoFormatted = passwordsInfoFormatted.replace(":", ": ")

        return passwordsInfoFormatted

    def returnToMainScreen(self):
        self.mainScr = mainScreen.MainScreen()
        self.close()