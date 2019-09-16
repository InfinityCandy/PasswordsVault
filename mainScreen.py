from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class mainScreen(QWidget):
    def __init__(self, windowWidth, windowHeigh):
        super().__init__()

        #Attributes
        self.windowWidth = windowWidth
        self.windowHeigh = windowHeigh
        self.MarginButtonsLeft = 20
        self.buttonHeigh = 32
        self.buttonWidth = (windowWidth/2) - self.MarginButtonsLeft
        self.MarginButtonsTop = (self.windowHeigh/3) - self.buttonHeigh 
        self.spaceBtwButtonsX = self.buttonWidth + self.MarginButtonsLeft

        #This method is executed when the class object is created
        self.initUI()

    def initUI(self):
        print(self.MarginButtonsTop)
        storeNewPaswordbtn = QPushButton('Store New password', self)
        storeNewPaswordbtn.clicked.connect(self.storeNewPassword)
        storeNewPaswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        storeNewPaswordbtn.move(self.MarginButtonsLeft, self.MarginButtonsTop) 
        

        searchPasswordbtn = QPushButton('Search Password', self) 
        searchPasswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        searchPasswordbtn.move(self.spaceBtwButtonsX, self.MarginButtonsTop)

        updatePasswordbtn = QPushButton('Update Password', self)
        updatePasswordbtn.resize(self.buttonWidth, self.buttonHeigh)
        updatePasswordbtn.move(self.MarginButtonsLeft, (self.MarginButtonsTop * 3) + self.buttonHeigh)

        deletePasswotdbtn = QPushButton('Delete Password', self)
        deletePasswotdbtn.resize(self.buttonWidth, self.buttonHeigh)
        deletePasswotdbtn.move(self.spaceBtwButtonsX, (self.MarginButtonsTop * 3) + self.buttonHeigh)
        
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('PasswordsVault')    
        self.show()

    def storeNewPassword(self):
        
