from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox

from passwordsOperator import PasswordsOperator


class StoreNewPassword(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 200
        self.windowHeigh = 300


        #This method is executed when the class's object is created
        self.drawWindow()

    def drawWindow(self):
        #Draws label and text box for site's name
        sitenNamelabel = QLabel(self)
        sitenNamelabel.setText("Site Name")
        sitenNamelabel.move(20, 0)
        self.siteNameTxtBox = QLineEdit(self)
        self.siteNameTxtBox.resize(165, 25)
        self.siteNameTxtBox.move(20, 25)

        #Draws label and textbox for email or username
        emailOrUserLabel = QLabel(self)
        emailOrUserLabel.setText("Email or UserName")
        emailOrUserLabel.move(20, 60)
        self.emailOrUserTextbox = QLineEdit(self)
        self.emailOrUserTextbox.resize(165, 25)
        self.emailOrUserTextbox.move(20, 85)

        #Draws label and textbox for password
        passwordLabel = QLabel(self)
        passwordLabel.setText("Password")
        passwordLabel.move(20, 120)
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.resize(165, 25)
        self.passwordTextBox.move(20, 145)

        #Draws label and textbox for confirm password
        confirmPasswordLabel = QLabel(self)
        confirmPasswordLabel.setText("Confirm Password")
        confirmPasswordLabel.move(20, 180)
        self.confirmPasswordTextBox = QLineEdit(self)
        self.confirmPasswordTextBox.setEchoMode(QLineEdit.Password)
        self.confirmPasswordTextBox.resize(165, 25)
        self.confirmPasswordTextBox.move(20, 205)

        #Draws the button to store the password and associates a event to it
        storePasswordbtn = QPushButton("Store Password", self)
        storePasswordbtn.clicked.connect(self.storePassword)
        storePasswordbtn.resize(165, 25)
        storePasswordbtn.move(20, 245)

        #Draws the window
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle('PasswordsVault - Store New Password')    
        self.show()
    
    #Check if all the fields were filled if not returns false
    #@return false/true: Return a boolean value, True if all the fields were filled or False otherwise
    def checkFieldsValues(self):
        #print(self.siteNameTxtBox.text())
        validInput = False
        if((self.siteNameTxtBox.text() == "") or (self.emailOrUserTextbox.text() == "") or (self.passwordTextBox.text() == "") or (self.confirmPasswordTextBox.text() == "")):
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
            
    
    def storePassword(self):
        if(self.checkFieldsValues()):
            passwordsOperator = PasswordsOperator()
            passwordsOperator.storePassword(self.siteNameTxtBox.text(), self.emailOrUserTextbox.text(), self.passwordTextBox.text())

            mainScreen = storeNewPassword.MainScreen()
        
