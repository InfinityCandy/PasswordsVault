from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox

import passwordsOperator
import mainScreen


class StoreNewPassword(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 200
        self.windowHeigh = 300


        #This method is executed when the class's object is created
        self.drawWindow()

    #Draws the screen to store a new password
    def drawWindow(self):
        #Draws the button to go back
        backbtn = QPushButton("Go back", self)
        backbtn.clicked.connect(self.goBack)
        backbtn.resize(80, 25)
        backbtn.move(120, 5)

        #Draws label and textbox for site's name
        sitenNameLabel = QLabel(self)
        sitenNameLabel.setText("Site Name")
        sitenNameLabel.setFixedSize(165, 25)
        sitenNameLabel.move(20, 25)
        self.siteNameTxtBox = QLineEdit(self)
        self.siteNameTxtBox.resize(165, 25)
        self.siteNameTxtBox.move(20, 50)

        #Draws label and textbox for email or username
        emailOrUserLabel = QLabel(self)
        emailOrUserLabel.setText("Email or UserName")
        emailOrUserLabel.setFixedSize(165, 25)
        emailOrUserLabel.move(20, 85)
        self.emailOrUserTextBox = QLineEdit(self)
        self.emailOrUserTextBox.resize(165, 25)
        self.emailOrUserTextBox.move(20, 110)

        #Draws label and textbox for password
        passwordLabel = QLabel(self)
        passwordLabel.setText("Password")
        passwordLabel.setFixedSize(165, 25)
        passwordLabel.move(20, 145)
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.resize(165, 25)
        self.passwordTextBox.move(20, 170)

        #Draws label and textbox for confirm password
        confirmPasswordLabel = QLabel(self)
        confirmPasswordLabel.setText("Confirm Password")
        confirmPasswordLabel.setFixedSize(165, 25)
        confirmPasswordLabel.move(20, 205)
        self.confirmPasswordTextBox = QLineEdit(self)
        self.confirmPasswordTextBox.setEchoMode(QLineEdit.Password)
        self.confirmPasswordTextBox.resize(165, 25)
        self.confirmPasswordTextBox.move(20, 230)

        #Draws the button to store the password and associates a event to it
        storePasswordbtn = QPushButton("Store Password", self)
        storePasswordbtn.clicked.connect(self.storePassword)
        storePasswordbtn.resize(165, 25)
        storePasswordbtn.move(20, 265)

        #Draws the window
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('Store New Password')    
        self.show()
    
    #Check if all the fields were filled if not returns false
    #@return false/true: Return a boolean value, True if all the fields were filled or False otherwise
    def checkFieldsValues(self):
        validInput = False

        if((self.siteNameTxtBox.text() == "") or (self.emailOrUserTextBox.text() == "") or (self.passwordTextBox.text() == "") or (self.confirmPasswordTextBox.text() == "")):
            error = QMessageBox()
            error.setText("Fill all fields")
            error.exec_()

            return validInput
        elif(self.passwordTextBox.text() != self.confirmPasswordTextBox.text()):
            error = QMessageBox()
            error.setText("The passwords doesn't match")
            error.exec_()

            return validInput
        else:
            validInput = True
            
            return validInput
            
    #Function that triggers when the store password button is clicked
    def storePassword(self):
        if(self.checkFieldsValues()):
            passwordsOpert = passwordsOperator.PasswordsOperator()
            passwordsOpert.storePassword(self.siteNameTxtBox.text(), self.emailOrUserTextBox.text(), self.passwordTextBox.text())

            self.mainScr = mainScreen.MainScreen()
            self.close()

    #Function that allows the user to go back to the main screen
    def goBack(self):
        self.mainScr = mainScreen.MainScreen()
        self.close()

        
