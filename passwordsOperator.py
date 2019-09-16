from PyQt5.QtWidgets import QMessageBox
import crypt
import os

class PasswordsOperator:

    def __init__(self):
        self.containerDirectory = "storedPasswords/"
        self.fileName = "Passwords.txt"

    #Function that stores a new password into the "Passwords.txt" file
    def storePassword(self, site, emailOrUser, password):
        #We first validate is the container folder exist
        #In thtat contianer folder is where we are going to store our passwords file
        if not os.path.exists(self.containerDirectory):
            os.makedirs(self.containerDirectory)

        #We validate if the file where the passwords are stored exists
        #If not exists then we create a new file with the first password
        if not os.path.exists(self.containerDirectory + self.fileName):
            passwordsFile = open(self.containerDirectory + self.fileName, "w")
            passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + crypt.crypt(password, "encrypt") + "\r\n")
            passwordsFile.close()

        #If the file exist then we append the new password to the end of it
        else:
            #We append the new password to the password's file
            passwrodsFile = open(self.containerDirectory + self.fileName, "a+")
            passwrodsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + crypt.crypt(password, "encrypt") + "\r\n")
        

        succesAlert = QMessageBox()
        succesAlert.setText("Password Stored Successfully")
        succesAlert.exec_()