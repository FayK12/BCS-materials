#this code takes a message and encrypts it, and can take an encrypted message to decrypt it. The messages are linked to a 4-digit key
#and are necessary for the encryption/decryption
def encryptor (mode, message, key):
        mod_key = (key%26)+1  #a mod_key is modified based on the key entered by user
        coded_msg = str()
        for char in message: 
            if char == ' ':
                coded_msg = coded_msg + ' '
            elif char != ' ':
                my_letter_ord = ord(char) #if char in msg is not a space, then character is turned into it's ASCII number equivalent
                if mode ==1:
                    coded_msg = coded_msg + chr(my_letter_ord - mod_key) #ASCII number less modified key determine a new number, which is turned into a character
                elif mode ==2:
                    coded_msg = coded_msg + chr(my_letter_ord + mod_key) #ASCII number plus modified key determine a new number, which is turned into a character
                    #print(coded_msg)        
        return coded_msg

userchoice = 0
message = str() #this empty string will store the return value of encryptor. Necessary.
print("~~~~~~WELCOME to the Encryptor!~~~~~~")
print()
print("NOTE: Only letters and spaces will be accepted as message input!")
while (userchoice !=3) and (userchoice < 3):
    print()
    print("========Main Menu=======")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    print()
    userchoice = int(input("Enter your choice => "))

    if userchoice == 1: #encryption flow
        message = input("Enter a message to encrypt: ")
        key = int(input("Enter a 4-digit key: "))
        print("Encrypting...")
        message = encryptor(1,message,key) #message will store the returned valued of the function. Necessary. Calling the function alone doesn't store the returned
        print()                                 #value of coded_msg into encryptor. Must store it in a global var. Functions don't store value. They can only be called
        print("Your encrypted message is: ")
        print(message)
        print()
        print("Returning to the main menu..")
    elif userchoice ==2: #decryption flow
        message = input("Enter a message to decrypt: ")
        key = int(input("Enter a 4-digit key: "))
        print("Decrypting...")
        message = encryptor(2,message,key) #message will store the returned valued of the function. Necessary.
        print()
        print("Your decrypted message is: ")
        print(message)
        print()
        print("If this isn't the right message, you have the wrong key.")
        print()
        print("Returning to the main menu..")
    elif userchoice ==3:
        print("Goodbye.")
    elif (userchoice > 3):
        print("Invalid choice. Farewell.")
    

