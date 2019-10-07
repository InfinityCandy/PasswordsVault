from PyQt5.QtWidgets import QMessageBox
import os
import caesarChiper

class PasswordsOperator:

    def __init__(self):
        self.containerDirectory = "storedPasswords/"
        self.fileName = "Passwords.txt"

    #Stores a new password into the "Passwords.txt" file, the file to be stored are: Site name, Email/UserName (could be any of both) and the password associated to that Email/UserName
    #@param site: Site's name which that account belongs
    #@param emailOrUser: Email or Username associated with that account
    #@param password: Password to be sotored
    def storePassword(self, site, emailOrUser, password):
        chiper = caesarChiper.CaesarCipher()

        #We first validate is the container folder exist
        #In thtat contianer folder is where we are going to store our passwords file
        if not os.path.exists(self.containerDirectory):
            os.makedirs(self.containerDirectory)
            
            passwordsFile = open(self.containerDirectory + self.fileName, "w")
            passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + chiper.encrypt(password) + "\r\n")
            passwordsFile.close()


            #We validate if the file where the passwords are stored exists
            #If not exists then we create a new file with the first password
        elif not os.path.exists(self.containerDirectory + self.fileName):
            passwordsFile = open(self.containerDirectory + self.fileName, "w")
            passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + chiper.encrypt(password) + "\r\n")
            passwordsFile.close()

        #If the file exist then we append the new password to the end of it
        else:
            #We append the new password to the password's file
            passwrodsFile = open(self.containerDirectory + self.fileName, "a+")
            passwrodsFile.write("Site Name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + chiper.encrypt(password) + "\r\n")
        

        succesAlert = QMessageBox()
        succesAlert.setText("Password Stored Successfully")
        succesAlert.exec_()

    #Function that searchs for any match of the Email/UserName or Site Name in the "Passwords.txt" file
    #@param searchByValue: Value used to search the password, could be the values "Email/UserName" or "Site Name"
    #@param valueToSearch: Value to be searched, could be an Email/UserName or the name of a Site
    #return passwordInfoFound or a String: If there is no stored passwords the method returns "404", if no password is found the method returns "403"
    #If we find one or more matchs we return an array with all of them
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

                    #If we found any value that match, we decrypt the password, and we append the password information to the list of found password
                    if(arrayValue == valueToSearch):
                        chiper = caesarChiper.CaesarCipher()
                        passwordInfoDecryptedPass = chiper.decrypt(passwordInfo)
                        
                        passwordInfoFound.append(passwordInfoDecryptedPass)

                #If the variable, where we were going to store the passwords once we found them has a length value of "0"
                #That means that we didn't find any password that match, so we return "405"
                if(len(passwordInfoFound) == 0):
                    return "405"
                #If we find the password/s we just return it as a string
                else:
                    return passwordInfoFound
        
        else:
            return "404"

    #Update an existing password in the Passwords.txt file, using the Email/UserName as reference
    #@param emailUserName: Email or Username which we want to update the associated password
    #@param newPassword: New password value that's going to replace the old one associted with the given Email/Username
    #@param String: A string that can be "200" which means that the password has been updated, "404" which means that we couldn't find the given Email/Username
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

                    #If we find any value that match we replace the second value in the array, which corresponds to the Password, with the new password
                    #We firts encrypt the new password
                    #And we change the "passwordUpdate" flag to write a new Passwords.txt file further in the code
                    if(emailUserNameValue == emailUserName):
                        chiper = caesarChiper.CaesarCipher()
                        passwordsInfoArray[2] = "Password: " + chiper.encrypt(newPassword)
                        passwordUpdate = True

                    #We create a new string which will contain the new Passwords.txt file text
                    newFileContent = newFileContent + (" - ".join(passwordsInfoArray)) + "\r\n"

                #If we could update the password by finding the Email/UserName associated to it, we write a new file, overwriting the old one, with the new information
                #And we return a status of 200
                if(passwordUpdate):
                    passwordsFile = open(self.containerDirectory + self.fileName, "w")
                    passwordsFile.write(newFileContent)
                    passwordsFile.close()
                    
                    return "200"
                else:
                    return "404"

    #Delete an existin password in the Passwords.txt file, using the Email/Username as reference to search for it
    #@param emailUserName: Email or Username used for searching the desire password and next delete it
    #@return String: An String tha can be "200" which means that the password has been deleted or "404" which means that there is not match for the given "Email/Username"
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
                        newFileContent = newFileContent + (" - ".join(passwordsInfoArray)) + "\r\n"
                        passwordDeleted = True

                
                #If we could delete the password by finding the Email/UserName associated to it, we write a new file, overwriting the old one, with the new information
                #And we return a status of 200
                if(passwordDeleted):
                    passwordsFile = open(self.containerDirectory + self.fileName, "w")
                    passwordsFile.write(newFileContent)
                    passwordsFile.close()
                    
                    return "200"
                else:
                    return "404"

    #Validates the existance of the "Passwords.txt" file and its container folder
    def validatePasswordsFilesExistance(self):
        #If the directory or file where the passwords are stored doesn't exist we return "404"
        if not os.path.exists(self.containerDirectory):
            return False
        elif not os.path.exists(self.containerDirectory + self.fileName):
            return False
        else:
            return True

