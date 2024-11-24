import os

def welcome():
    '''Prints the welcome message'''
    print("Welcome To Caesar Cipher")
    print("This Program Encrypts Or Decrypts Text Using Caesar Cipher.")
    print()

#Defining the possible characters used in cipher
chrs = 'abcdefghijklmnopqrstuvwxyz'
num_chrs = len(chrs)


def enter_message():
    '''Function to check encrypted or decrypted values based on user input and shift key'''
    while True:
        enc_or_dec = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        print()
        #Run encryption mode if e is selected
        if enc_or_dec == 'e':
            print("Encryption Mode")
            print()
            #call message_or_file() function while passing the parameter
            read_medium, shift_num, text = message_or_file()

            #if read from file is choosen as medium
            if read_medium == 'f':
                while True:
                    filename = input("Enter a filename: ")
                    if is_file(filename):
                        #run process_file function passing file name and mode (encryption or decryption)
                        ch = process_file(filename, enc_or_dec)
                        #call continue_or_exit function to confirm whether or not they want to continue
                        continue_or_exit()
                         
                    else:
                        print("Invalid Filename")
                break

            #if from console is selected as medium
            elif read_medium == 'c':
                #Prompt to enter shift key and pass the value through encrypt function
                try:
                    shift_num = int(shift_num)
                    ciphertext = encrypt(text, shift_num)
                    print(f'CIPHERTEXT: {ciphertext}')
                    continue_or_exit()
                #Incase of value error
                except ValueError:
                    print("Key must be an integer")
                    continue
        #If decryption mode is selected
        elif enc_or_dec == 'd':
            print("Decryption Mode")
            print()
            #call message_or_file() function while passing the parameter
            read_medium, shift_num, text = message_or_file()
            
            
            #if from file is selected as medium
            if read_medium == 'f':
                while True:
                    filename = input("Enter a filename: ")
                    if is_file(filename):
                        ch = process_file(filename, enc_or_dec)
                        continue_or_exit()
                    else:
                        print("Invalid Filename")
                break
                        
            #if console is choosen as medium
            elif read_medium == 'c':
                try:
                    shift_num = int(shift_num)
                    plaintext = decrypt(text, shift_num)
                    print(f'PLAINTEXT: {plaintext}')
                    continue_or_exit()
                #in case of value error in shift number
                except ValueError:
                    print("Shift number must be an integer")
                    continue

        else:
            print("Invalid option")
            continue


def encrypt(plaintext,shift_num):
    '''Function for encrypting the text'''
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        #If character is not blank space ' '
        if not letter == ' ':
            index = chrs.find(letter)
            #Cipher the text
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + shift_num
                if new_index >= num_chrs:
                    new_index -= num_chrs
                ciphertext += chrs[new_index]
    #Return the ciphered text
    return ciphertext


def decrypt(ciphertext,shift_num):
    '''Function for decrypting the text'''
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        #If character is not blank space ' '
        if not letter == ' ':
            index = chrs.find(letter)
            #Convert to plain text
            if index == -1:
                plaintext += letter
            else:
                new_index = index - shift_num
                if new_index < 0:
                    new_index += num_chrs
                plaintext += chrs [new_index]
    #return the plaintext
    return plaintext


def process_file(file, mode):
    '''Function for processing shift key after reading from file'''
    str1 = []
    #open file in read mode
    with open(file, 'r') as f_file:
        msg = f_file.read().lower()

        while True:
            #Take shift key and convert msg into list of encrypted/decrypted message
            try:
                key = int(input("What is the shift number: "))
                for char in msg:
                    if char == chr(32):
                        str1.append(" ")
                    elif char == chr(10):
                        str1.append("\n")
                    else:
                        str1.append(encrypt(char, key))
                break
            except ValueError:
                print("Invalid Shift")
    #Write the result in result.txt
    text_output = 'results.txt'
    with open(text_output, 'w') as file:
        for i in str1:
            file.write(i)

    print(f"Output written to {(text_output)}")
    return str1

def is_file(file):
    '''Function to check if file exists or not'''
    return os.path.isfile(file)


def write_messages(string):
    '''function to write message in the file'''
    with open('results.txt', 'w') as file:
        for i in string:
            file.write(i)


def message_or_file():
    '''function to check if user wants to read from file or console'''
    while True:
        #prompt to check if user wants to read from file or console
        read_medium = input("Would you like to read from a file (f) or the console (c)? ").lower()
        #if file is selected
        if read_medium == 'f':
            return 'f', None, None
        #if console is selected
        elif read_medium == 'c':
            try:
                text = input("What message would you like to encrypt/decrypt: ")
                shift_num = int(input("What is the shift key: "))
                    
                return 'c', shift_num, text
            except ValueError:
                print("Key must be an integer")
                continue
        else:
            print("Invalid, please enter either 'f' or 'c'")
            continue


def continue_or_exit():
    '''function to ask user to continue or exit'''
    while True:
        continue_or_not = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if continue_or_not == 'n':
            print("Thanks for using the program, goodbye!")
            exit()
        elif continue_or_not == 'y':
            enter_message()
            
        else:
            print("Invalid option (choose either 'y' or 'n')")


if __name__ == "__main__":
     welcome()
     enter_message()