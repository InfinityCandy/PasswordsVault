import crypt
import os

class PasswordsOperator:
    filePath = "StoredPasswords/Passwords.txt"

    def storePassword(self, site, emailOrUser, password):
        passwordsFile = open(filePath, "w")
        passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + crypt.crypt(password, "encrypt"))
        passwordsFile.close()

        print("Password saved")