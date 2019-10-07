from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QMessageBox

import mainScreen
import passwordsOperator

class DeletePassword(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 200
        self.windowHeigh = 200


        #This method is executed when the class's object is created
        self.drawWindow()

    #Draws the window to delete a stored password
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

        #Draws the button to search password by Email/UserName
        deletePasswordbtn = QPushButton("Delete Password", self)
        deletePasswordbtn.clicked.connect(self.deleteStoredPassword)
        deletePasswordbtn.resize(165, 25)
        deletePasswordbtn.move(20, 160)

        #Draws the window
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle("Delete Password")    
        self.show()

    #Function that allows the user to go back to the main screen
    def goBack(self):
        self.mainScr = mainScreen.MainScreen()
        self.close()

    #Check if all the fields of the form have been filled
    #@return True/False: Returns "True" if all the fields have been filled, and "False" otherwise
    def checkFieldsValues(self):
        validInput = False

        if(self.searchUserPasswordTextBox.text() == "" or self.confirmUserTextBox.text() == ""):
            error = QMessageBox()
            error.setText("Fill all fields")
            error.exec_()

            return validInput

        elif(self.searchUserPasswordTextBox.text() != self.confirmUserTextBox.text()):
            error = QMessageBox()
            error.setText("The Email/UserName doesn't match")
            error.exec_()

            return validInput

        else:
            validInput = True

            return validInput

    #Function that is called to delete a stored password, when the "delete password" button is pressed
    def deleteStoredPassword(self):
        if(self.checkFieldsValues()):
            passwordsOpert = passwordsOperator.PasswordsOperator()

            passwordDeleteResult = passwordsOpert.deletePassword(self.searchUserPasswordTextBox.text())

            if(passwordDeleteResult == "404"):
                error = QMessageBox()
                error.setText("Email/UserName didn't find")
                error.exec_()
            else:
                success = QMessageBox()
                success.setText("Password deleted successfully!")
                success.exec_()

                self.mainScr = mainScreen.MainScreen()
                self.close()
