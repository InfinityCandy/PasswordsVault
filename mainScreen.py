from PyQt5.QtWidgets import QPushButton, QMainWindow

import storeNewPassword

class MainScreen(QMainWindow):
    #Constructor
    def __init__(self):
        super().__init__()

        #Instance Attributes
        self.windowWidth = 400
        self.windowHeigh = 150

        #This method is executed when the class's object is created
        self.drawWindow()

    #Methods

    #Draws the Main Screen on the computer's screen 
    def drawWindow(self):
        storeNewPaswordbtn = QPushButton('Store new password', self)
        storeNewPaswordbtn.clicked.connect(self.storePassword)
        storeNewPaswordbtn.resize(165, 32)
        storeNewPaswordbtn.move(20, 40) 

        searchPasswordbtn = QPushButton('Search password', self) 
        searchPasswordbtn.resize(165, 32)
        searchPasswordbtn.move(215, 40)

        updatePasswordbtn = QPushButton('Update password', self)
        updatePasswordbtn.resize(165, 32)
        updatePasswordbtn.move(20, 82)

        deletePasswotdbtn = QPushButton('Delete password', self)
        deletePasswotdbtn.resize(165, 32)
        deletePasswotdbtn.move(215, 82)
        
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('PasswordsVault')    
        self.show()

    #The function related to "Store new password" button
    def storePassword(self):
        self.storeNewPasswordScreen = storeNewPassword.StoreNewPassword()

        #Close the current window
        self.close()
        
        
