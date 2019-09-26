from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QMessageBox

import mainScreen
import passwordsOperator

class UpdatePassword(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 200
        self.windowHeigh = 340


        #This method is executed when the class's object is created
        self.drawWindow()


    #Draws the screen to store a new password
    def drawWindow(self):
        #Draws the button to go back
        backbtn = QPushButton("Go back", self)
        backbtn.clicked.connect(self.goBack)
        backbtn.resize(80, 25)
        backbtn.move(120, 5)

        #Draws label and textbox for updating a password by Email/UserName
        searchUserPasswordLabel = QLabel(self)
        searchUserPasswordLabel.setText("Email/UserName")
        searchUserPasswordLabel.setFixedSize(165, 25)
        searchUserPasswordLabel.move(20, 35)
        self.searchUserPasswordTextBox = QLineEdit(self)
        self.searchUserPasswordTextBox.resize(165, 25)
        self.searchUserPasswordTextBox.move(20, 60)

        #Draws label and textbox for confirm Email/UserName
        confirmationUserLabel = QLabel(self)
        confirmationUserLabel.setText("Confirm Email/UserName")
        confirmationUserLabel.setFixedSize(165, 25)
        confirmationUserLabel.move(20, 100)
        self.confirmUserTextBox = QLineEdit(self)
        self.confirmUserTextBox.resize(165, 25)
        self.confirmUserTextBox.move(20, 125)

        #Draws label and textbox for the new password
        newPasswordLabel = QLabel(self)
        newPasswordLabel.setText("New Password")
        newPasswordLabel.setFixedSize(165, 25)
        newPasswordLabel.move(20, 165)
        self.newPasswordTextBox = QLineEdit(self)
        self.newPasswordTextBox.setEchoMode(QLineEdit.Password)
        self.newPasswordTextBox.resize(165, 25)
        self.newPasswordTextBox.move(20, 190)

        #Draws label and textbox for confirm password
        confirmNewPasswordLable = QLabel(self)
        confirmNewPasswordLable.setText("Confirm New Password")
        confirmNewPasswordLable.setFixedSize(165, 25)
        confirmNewPasswordLable.move(20, 230)
        self.confirmPasswordTextBox = QLineEdit(self)
        self.confirmPasswordTextBox.setEchoMode(QLineEdit.Password)
        self.confirmPasswordTextBox.resize(165, 25)
        self.confirmPasswordTextBox.move(20, 255)

        #Draws the button to search password by Email/UserName
        updatePasswordbtn = QPushButton("Update Password", self)
        updatePasswordbtn.clicked.connect(self.updateStoredPassword)
        updatePasswordbtn.resize(165, 25)
        updatePasswordbtn.move(20, 295)

        #Draws the window
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle("Search Password")    
        self.show()

    #Function that allows the user to go back to the main screen
    def goBack(self):
        self.mainScr = mainScreen.MainScreen()
        self.close()

    def checkFieldsValues(self):
        validInput = False

        if(self.searchUserPasswordTextBox.text() == "" or self.confirmUserTextBox.text() == "" or self.newPasswordTextBox.text() == "" or self.confirmPasswordTextBox.text() == ""):
            error = QMessageBox()
            error.setText("Fill all fields")
            error.exec_()

            return validInput

        elif(self.searchUserPasswordTextBox.text() != self.confirmUserTextBox.text()):
            error = QMessageBox()
            error.setText("The Email/UserName doesn't match")
            error.exec_()

            return validInput

        elif(self.newPasswordTextBox.text() != self.confirmPasswordTextBox.text()):
            error = QMessageBox()
            error.setText("The new passwords doesn't match")
            error.exec_()

            return validInput
        else:
            validInput = True

            return validInput

    def updateStoredPassword(self):
        if(self.checkFieldsValues()):
            passwordsOpert = passwordsOperator.PasswordsOperator()

            passwordUpdateResult = passwordsOpert.updatePassword(self.searchUserPasswordTextBox.text(), self.newPasswordTextBox.text())

            if(passwordUpdateResult == "404"):
                error = QMessageBox()
                error.setText("Email/UserName didn't find")
                error.exec_()
            else:
                success = QMessageBox()
                success.setText("Password updated successfully!")
                success.exec_()

                self.mainScr = mainScreen.MainScreen()
                self.close()
