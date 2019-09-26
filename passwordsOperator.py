from PyQt5.QtWidgets import QMessageBox
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
            
            passwordsFile = open(self.containerDirectory + self.fileName, "w")
            passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + password + "\r\n")
            passwordsFile.close()


            #We validate if the file where the passwords are stored exists
            #If not exists then we create a new file with the first password
        elif not os.path.exists(self.containerDirectory + self.fileName):
            passwordsFile = open(self.containerDirectory + self.fileName, "w")
            passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + password + "\r\n")
            passwordsFile.close()

        #If the file exist then we append the new password to the end of it
        else:
            #We append the new password to the password's file
            passwrodsFile = open(self.containerDirectory + self.fileName, "a+")
            passwrodsFile.write("Site Name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + password + "\r\n")
        

        succesAlert = QMessageBox()
        succesAlert.setText("Password Stored Successfully")
        succesAlert.exec_()

    def searchPassword(self, searchByValue, valueToSearch):
        #If the directory or file where the passwords are stored doesn't exist we return "404"
        if (self.validatePasswordsFilesExistance()):
            passwordsFile = open(self.containerDirectory + self.fileName, "r")

            if(passwordsFile.mode == "r"):
                passwordsInfoArray = []

                fileContent = passwordsFile.read()

                #We first clean the content from white spaces
                fileContent = fileContent.replace(" ", "")
                #We split every password information, each one of them are stores separated by new lines
                fileContent = fileContent.split("\n")

                #We use "-1" in our for cicle to avoid adding and empty new line to the array
                for i in range(len(fileContent) - 1):
                    passwordsInfoArray.append(fileContent[i].split("-"))
                
                #We define the index that we are going to use to search in the passwordsInfoArray
                #The index is defined by the value selected by the user on the searchPasswordScreen's combobox
                if(searchByValue == "Site Name"):
                    searchByIndex = 0
                else:
                    searchByIndex = 1
                
                #Variable where the searched password is going to be stored
                passwordInfoFound = []

                #We iterate throw every element in the passwordsInfoArray
                for passwordInfo in passwordsInfoArray:
                    
                    #We split the value "searchByIndex", that we setted above, in the "passwordInfo" array
                    arrayValue = passwordInfo[searchByIndex].split(":")
                    #We take the second value from the element in the array, which corresponds to the "Site Name" or "Emial/UserName" value
                    arrayValue = arrayValue[1]

                    #If we found any value that match, we join every element in the array where is that value, using "-" to separate each value
                    #And qe append the password String to the array
                    if(arrayValue == valueToSearch):
                        passwordInfoFound.append(passwordInfo)

                #If the variable, where we were going to store the passwords once we found them has a length value of "0"
                #That means that we didn't find any password that match, so we return "405"
                if(len(passwordInfoFound) == 0):
                    return "405"
                #If we find the password/s we just return it as a string
                else:
                    return passwordInfoFound
        
        else:
            return "404"

    def updatePassword(self, emailUserName, newPassword):
        if(self.validatePasswordsFilesExistance()):
            passwordsFile = open(self.containerDirectory + self.fileName, "r")

            if(passwordsFile.mode == "r"):
                passwordsInfoArray = []

                fileContent = passwordsFile.read()

                #We first clean the content from white spaces
                fileContent = fileContent.replace(" ", "")
                #We split every password information, each one of them are stores separated by new lines
                fileContent = fileContent.split("\n")

                #We create a flag to know if we successfully updated the password
                passwordUpdate = False
                newFileContent = ""

                #We use "-1" in our for cicle to avoid adding and empty new line to the array
                for i in range(len(fileContent) - 1):
                    passwordsInfoArray = fileContent[i].split("-")
                    
                    #We split the value of Email/UserName
                    emailUserNameMap = passwordsInfoArray[1].split(":")
                    #We take the second value from the element in the array, which corresponds to the "Emial/UserName" value
                    emailUserNameValue = emailUserNameMap[1]

                    #If we found any value that match, we join every element in the array where is that value, using "-" to separate each value
                    #And qe append the password String to the array
                    if(emailUserNameValue == emailUserName):
                        passwordsInfoArray[2] = "Password: " + newPassword
                        passwordUpdate = True

                    #We create a new string which containes the new text in the file
                    newFileContent = newFileContent + ("-".join(passwordsInfoArray)) + "\r\n"

                #If we could update the password by finding the Email/UserName associated to it, we write a new file, overwriting the old one, with the new information
                #And we return a status of 200
                if(passwordUpdate):
                    passwordsFile = open(self.containerDirectory + self.fileName, "w")
                    passwordsFile.write(newFileContent)
                    passwordsFile.close()
                    
                    return "200"
                else:
                    return "404"

    def deletePassword(self, emailUserName):
        if(self.validatePasswordsFilesExistance()):
            passwordsFile = open(self.containerDirectory + self.fileName, "r")

            if(passwordsFile.mode == "r"):
                passwordsInfoArray = []

                fileContent = passwordsFile.read()

                #We first clean the content from white spaces
                fileContent = fileContent.replace(" ", "")
                #We split every password information, each one of them are stores separated by new lines
                fileContent = fileContent.split("\n")

                #We create a flag to know if we successfully updated the password
                passwordDeleted = False
                newFileContent = ""

                #We use "-1" in our for cicle to avoid adding and empty new line to the array
                for i in range(len(fileContent) - 1):
                    passwordsInfoArray = fileContent[i].split("-")
                    
                    #We split the value of Email/UserName
                    emailUserNameMap = passwordsInfoArray[1].split(":")
                    #We take the second value from the element in the array, which corresponds to the "Emial/UserName" value
                    emailUserNameValue = emailUserNameMap[1]

                    #For every value that doesn't match we add it to the the new file content
                    if(emailUserNameValue != emailUserName):
                        newFileContent = newFileContent + ("-".join(passwordsInfoArray)) + "\r\n"
                        passwordDeleted = True

                
                #If we could update the password by finding the Email/UserName associated to it, we write a new file, overwriting the old one, with the new information
                #And we return a status of 200
                if(passwordDeleted):
                    passwordsFile = open(self.containerDirectory + self.fileName, "w")
                    passwordsFile.write(newFileContent)
                    passwordsFile.close()
                    
                    return "200"
                else:
                    return "404"

                
    def validatePasswordsFilesExistance(self):
        #If the directory or file where the passwords are stored doesn't exist we return "404"
        if not os.path.exists(self.containerDirectory):
            return False
        elif not os.path.exists(self.containerDirectory + self.fileName):
            return False
        else:
            return True

