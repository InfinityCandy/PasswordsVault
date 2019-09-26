from PyQt5.QtWidgets import QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox

import mainScreen
import passwordsOperator
import showPasswordInfo

class SearchPassword(QMainWindow):
    def __init__(self):
        super().__init__()

        #Attributes
        self.windowWidth = 200
        self.windowHeigh = 200


        #This method is executed when the class's object is created
        self.drawWindow()

    #Draws the screen to store a new password
    def drawWindow(self):
        #Draws the button to go back
        backbtn = QPushButton("Go back", self)
        backbtn.clicked.connect(self.goBack)
        backbtn.resize(80, 25)
        backbtn.move(120, 5)

        #Draws the combobox to indicate which field use to do the search
        searchPasswordLabel = QLabel(self)
        searchPasswordLabel.setText("Search by")
        searchPasswordLabel.setFixedSize(165, 25)
        searchPasswordLabel.move(20, 30)
        self.searchOptionsComboBox = QComboBox(self)
        self.searchOptionsComboBox.addItem("Site Name")
        self.searchOptionsComboBox.addItem("Email/UserName")
        self.searchOptionsComboBox.setFixedSize(165, 25)
        self.searchOptionsComboBox.move(15, 50)

        #Draws label and texbox for searching a password
        searchPasswordLabel = QLabel(self)
        searchPasswordLabel.setText("Value to Search")
        searchPasswordLabel.setFixedSize(165, 25)
        searchPasswordLabel.move(20, 85)
        self.searchPasswordTxtBox = QLineEdit(self)
        self.searchPasswordTxtBox.resize(165, 25)
        self.searchPasswordTxtBox.move(20, 105)

        #Draws the button to store the password and associates an event to it
        searchPasswordbtn = QPushButton("Search Password", self)
        searchPasswordbtn.clicked.connect(self.searchForPassword)
        searchPasswordbtn.resize(165, 25)
        searchPasswordbtn.move(20, 150)

        #Draws the window
        self.setGeometry(200, 200, self.windowWidth, self.windowHeigh)
        self.setWindowTitle("Search Password")    
        self.show()


    #Function that allows the user to go back to the main screen
    def goBack(self):
        self.mainScr = mainScreen.MainScreen()
        self.close()

    def searchForPassword(self):
        passwordsOpert = passwordsOperator.PasswordsOperator()

        passwordSearchResult = passwordsOpert.searchPassword(self.searchOptionsComboBox.currentText(), self.searchPasswordTxtBox.text())

        #In case the file or folder where the passwords are stored doesn't exists, then we get a 404 error from the method above
        if(passwordSearchResult == "404"):
            error = QMessageBox()
            error.setText("There's no passwords stored")
            error.exec_()
        elif (passwordSearchResult == "405"):
            error = QMessageBox()
            error.setText("No password found for that Site or UserName/Email")
            error.exec_()
        else:
            self.showPasswordInfoScr = showPasswordInfo.ShowPasswordInfo(passwordSearchResult)
            self.close()
            
