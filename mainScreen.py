from PyQt5.QtWidgets import QPushButton, QMainWindow

import storeNewPassword
import searchPassword
import updatePassword
import deletePassword

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
        searchPasswordbtn.clicked.connect(self.searchForPassword)
        searchPasswordbtn.resize(165, 32)
        searchPasswordbtn.move(215, 40)

        updatePasswordbtn = QPushButton('Update password', self)
        updatePasswordbtn.clicked.connect(self.updateStoredPassword)
        updatePasswordbtn.resize(165, 32)
        updatePasswordbtn.move(20, 82)

        deletePasswotdbtn = QPushButton('Delete password', self)
        deletePasswotdbtn.clicked.connect(self.deleteStoredPassword)
        deletePasswotdbtn.resize(165, 32)
        deletePasswotdbtn.move(215, 82)
        
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('PasswordsVault')    
        self.show()

    #Function related to "Store new password" button
    def storePassword(self):
        self.storeNewPasswordScreen = storeNewPassword.StoreNewPassword()

        #Close the current window
        self.close()

    #Function realated to "Search password" button
    def searchForPassword(self):
        self.searchPasswordScreen = searchPassword.SearchPassword()

        #Close the current window
        self.close()

    #Function related to "Update password" button
    def updateStoredPassword(self):
        self.updateStoredPasswordScreen = updatePassword.UpdatePassword()

        #Close the current window
        self.close()

    #Function related to "Delete password" button
    def deleteStoredPassword(self):
        self.deleteStoredPasswordScreen = deletePassword.DeletePassword()

        #Close the current window
        self.close()
        
        
