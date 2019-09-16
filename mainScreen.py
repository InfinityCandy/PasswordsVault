from PyQt5.QtWidgets import QPushButton, QMainWindow

from storeNewPassword import StoreNewPassword

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 400
        self.windowHeigh = 150
        self.MarginButtonsLeft = 20
        self.buttonHeigh = 32
        self.buttonWidth = (self.windowWidth/2) - self.MarginButtonsLeft
        self.MarginButtonsTop = (self.windowHeigh/2) - self.buttonHeigh 
        self.spaceBtwButtonsX = self.buttonWidth + self.MarginButtonsLeft

        #This method is executed when the class's object is created
        self.drawWindow()

    #Methods
    def drawWindow(self):
        storeNewPaswordbtn = QPushButton('Store New password', self)
        storeNewPaswordbtn.clicked.connect(self.storeNewPassword)
        storeNewPaswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        storeNewPaswordbtn.move(self.MarginButtonsLeft, self.MarginButtonsTop) 

        searchPasswordbtn = QPushButton('Search Password', self) 
        searchPasswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        searchPasswordbtn.move(self.spaceBtwButtonsX, self.MarginButtonsTop)

        updatePasswordbtn = QPushButton('Update Password', self)
        updatePasswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        updatePasswordbtn.move(self.MarginButtonsLeft, self.MarginButtonsTop + self.buttonHeigh)

        deletePasswotdbtn = QPushButton('Delete Password', self)
        deletePasswotdbtn.resize(self.buttonWidth, self.buttonHeigh)
        deletePasswotdbtn.move(self.spaceBtwButtonsX, self.MarginButtonsTop + self.buttonHeigh)
        
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('PasswordsVault')    
        self.show()

    def storeNewPassword(self):
        self.storeNewPasswordScreen = StoreNewPassword()
        self.storeNewPasswordScreen.show()

        #Close the current window
        self.close()
        
        
