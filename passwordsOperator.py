import crypt
import os


class PasswordsOperator:
    def storePassword(self, site, emailOrUser, password):
        passwordsFile = open("Passwords.txt", "w")
        passwordsFile.write("Site name: " + site + " - Email/UserName: " + emailOrUser + " - Password: " + crypt.crypt(password, "encrypt"))
        passwordsFile.close()

        print("Password saved")