"""
author: Oriah Edry
Program name: En/Decryption-project
Description: A program that takes a text file as input and outputs a text file
Date: 19/10/2025
"""

# Import necessary modules for system arguments and logging
import sys
import logging
# Setting up the log file and its basic configuration
log_filename = 'log.txt'
logging.basicConfig(filename= log_filename,level = logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# The file used to store the encrypted message
Filename = 'encrypted_msg.txt'
# The dictionary for the encryption and make its opposite for the decryption
encryption_cypher = {'A': 56, 'B': 57, 'C': 58, 'D': 59, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46,
                     'L': 47, 'M': 48, 'N': 49, 'O': 60, 'P': 61, 'Q': 62, 'R': 63, 'S': 64, 'T': 65, 'U': 66, 'V': 67,
                     'W': 68, 'X': 69, 'Y': 10, 'Z': 11, 'a': 12, 'b': 13, 'c': 14, 'd': 15, 'e': 16, 'f': 17, 'g': 18,
                     'h': 19, 'i': 30, 'j': 31, 'k': 32, 'l': 33, 'm': 34, 'n': 35, 'o': 36, 'p': 37, 'q': 38, 'r': 39,
                     's': 90, 't': 91, 'u': 92, 'v': 93, 'w': 94, 'x': 95, 'y': 96, 'z': 97, ' ': 98, ',': 99,
                     '.': 100, "'": 101, '!': 102, '-': 103
                     }

decryption_cypher = {v: k for k, v in encryption_cypher.items()}


def letter_to_number():
    # Gets the message from the user
    message = input("enter message : ").lower()
    # Assertion: If invalid characters exist, the program will halt immediately
    invalid_chars = [char for char in message if char not in encryption_cypher]
    assert not invalid_chars

    # The encryption process, and saving it in a file
    e_message = [str(encryption_cypher[char]) for char in message]
    encrypted_content = ",".join(e_message)
    with open(Filename, 'w') as file:
        file.write(encrypted_content)
        logging.info('message has been encrypted successfully')


def num_to_letter():
    # Attempt to read the encrypted content from the file
    try:
        with open(Filename, 'r') as f:
            encrypted_content = f.read()
        # Check if the file is empty
        if not encrypted_content:
            print('this is an empty file')
            logging.warning('empty file')
            return
    except FileNotFoundError:
        # Handle case where the file does not exist
        logging.warning('file not found')
        print('there is no such file')
        return
    # Attempt to decrypt the content
    decrypt_massage = encrypted_content.split(",")
    decrypted_chars = [decryption_cypher[int(char)] for char in decrypt_massage]
    decrypted_message = "".join(decrypted_chars)
    print(decrypted_message) # Print decrypted message


def main():
    # List of valid command-line parameters
    allowed_parameters = ["encrypt", "decrypt"]
    try:
        # Get the action and convert to lowercase
        action = sys.argv[1].lower()
        if action in allowed_parameters:
            logging.info("the parameter is allowed")
            # Call the appropriate function based on the action
            if action == 'encrypt':
                letter_to_number()
            elif action == 'decrypt':
                num_to_letter()
        else:
            # Handle invalid parameter
            print("the parameter isn't allowed, please try again using encrypt/decrypt")
            logging.warning("an invalid parameter was entered ")
    except IndexError:
        # Handle missing parameter
        print("please enter a parameter(encrypt/decrypt)")
        logging.error("there is no such parameter")


if __name__ == '__main__':
    # Start the main execution of the program
    main()