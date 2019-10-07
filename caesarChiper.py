class CaesarCipher:
    def __init__(self):
        #Key used to decrypt and encrypt passwords
        self.key = 7

    #Encrypts a given password using the "self.key" to do it
    #@param plainPassword: A plain text password
    #@return encryptedPassword: The Encrypted password text
    def encrypt(self, plainPassword):
        encryptedPasswordArray = []
        passwordArray = list(plainPassword)

        for letter in passwordArray:
            letterASCIICode = ord(letter)
            newLetterASCIICode = letterASCIICode + self.key

            newLetterASCIICode = self.encryptASCIICodeAdjuter(newLetterASCIICode)
        
            encryptedPasswordArray.append(chr(newLetterASCIICode))
            
        encryptedPassword = "".join(encryptedPasswordArray)

        return encryptedPassword

    #Given an array with the password information (Site name, Email/UserName and Password) the function decripts the value that corresponds to the password
    #And returns and array with the password information
    #@param passwordInformation: An array with the password's information (Site Name:value, Email/UserName:value, Password:value) with the password value encrypted
    #@return passwordInformation: An array with the password's information, with the password value decripted
    def decrypt(self, passwordInformation):
        decryptedPasswordArray = []
        passwordValue = passwordInformation[2]
        passwordArray = list(passwordValue[9:])

        for letter in passwordArray:
            letterASCIICode = ord(letter)
            newLetterASCIICode = letterASCIICode - self.key

            newLetterASCIICode = self.encryptASCIICodeAdjuter(newLetterASCIICode)

            decryptedPasswordArray.append(chr(newLetterASCIICode))

        decryptedPassword = "".join(decryptedPasswordArray)
        passwordInformation[2] = "Password:" + decryptedPassword

        return passwordInformation


    #Validates an ensures that a lleter's ASCII code doesn't excced the ASCII code available values for UTF-8 (32 - 126) during ecryptation
    #@param ASCIICode: An ASCII code value
    #@return ASCIICode: A valid ASCII code between 32 and 126
    def encryptASCIICodeAdjuter(self, ASCIICode):
        if(ASCIICode > 126):
            return ((ASCIICode - 126) + 32)
        else:
            return ASCIICode

    #Validates an ensures that a lleter's ASCII code doesn't excced the ASCII code available values for UTF-8 (32 - 126) during decryptation
    #@param ASCIICode: An ASCII code value
    #@return ASCIICode: A valid ASCII code between 32 and 126
    def decryptASCIICodeAdjuster(self, ASCIICode):
        if(ASCIICode < 32):
            return (126 - (32 - ASCIICode))
        else:
            return ASCIICode