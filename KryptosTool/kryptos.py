# MrJ
# 10/11/2024
# Kryptos Encryption/Decryption Tool


def kryptos():
    # Kryptos Vigenere Table
    VIGENERE_TABLE = [
        ["K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P"],
        ["R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T"],
        ["Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O"],
        ["P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S"],
        ["T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A"],
        ["O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B"],
        ["S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C"],
        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D"],
        ["B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E"],
        ["C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F"],
        ["D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G"],
        ["E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H"],
        ["F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I"],
        ["G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L"],
        ["I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M"],
        ["J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N"],
        ["L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q"],
        ["M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U"],
        ["N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V"],
        ["Q", "U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W"],
        ["U", "V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X"],
        ["V", "W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z"],
        ["W", "X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K"],
        ["X", "Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R"],
        ["Z", "K", "R", "Y", "P", "T", "O", "S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "Q", "U", "V", "W", "X", "Z", "K", "R", "Y"]
    ]

    menu_selection = 0
    plain_text = ""
    cipher_text = ""
    key = ""

    while menu_selection != 5:
        display_menu()

        try:
            print()
            menu_selection = int(input("Select A Menu Option: ").strip())
        except ValueError:
            print("That is not a valid menu selection.")
            continue
            
        if menu_selection == 1:
            # Encrypt Text Using Vigenere Table and Key
            print()
            plain_text = input("Enter Text To Encrypt: ").strip()
            print()
            key = input("Enter Key: ").strip()
            cipher_text = encrypt(key, plain_text, VIGENERE_TABLE)
            print()
            print("**********************Key***********************")
            print(key)
            print("************************************************")
            print()
            print("*****************Encrypted Text*****************")
            print(cipher_text)
            print("************************************************")
            print()
            
        elif menu_selection == 2:
            # Encrypt Text Using Vigenere Table and Key
            print()
            print("Place a file called Keys.txt in the same directory.")
            print("Ensure each line is a different key.")
            print()
            plain_text = input("Enter Text To Encrypt: ").strip()
            
            # Open Keys.txt for processing
            keys = []
            with open("Keys.txt", "r") as infile:
                keys = infile.readlines()

            for line in keys:
                # Parse each key into encrypt()
                key = line.strip()
                cipher_text = encrypt(key, plain_text, VIGENERE_TABLE)
                
                with open("EncryptionResults.txt", "a") as outfile:
                    outfile.write("\n**********************Key***********************\n")
                    outfile.write(f"{key}\n")
                    outfile.write("************************************************\n")
                    outfile.write("\n*****************Encrypted Text*****************\n")
                    outfile.write(f"{cipher_text}\n")
                    outfile.write("************************************************\n\n")
            
        elif menu_selection == 3:
            # Decrypt Text Using Vigenere Table and Key
            print()
            cipher_text = input("Enter Text To Decrypt: ").strip()
            print()
            key = input("Enter Key: ").strip()
            plain_text = decrypt(key, cipher_text, VIGENERE_TABLE)
            print()
            print("**********************Key***********************")
            print(key)
            print("************************************************")
            print()
            print("*****************Decrypted Text*****************")
            print(plain_text)
            print("************************************************")
            print()
            
        elif menu_selection == 4:
            # Decrypt Text Using Vigenere Table and Key List
            print()
            print("Place a file called Keys.txt in the same directory.")
            print("Ensure each line is a different key.")
            print()
            cipher_text = input("Enter Text To Decrypt: ").strip()
            
            # Open Keys.txt for processing
            keys = []
            with open("Keys.txt", "r") as infile:
                keys = infile.readlines()

            for line in keys:
                # Parse each key into decrypt()
                key = line.strip()
                plain_text = decrypt(key, cipher_text, VIGENERE_TABLE)
                
                with open("DecryptionResults.txt", "a") as outfile:
                    outfile.write("\n**********************Key***********************\n")
                    outfile.write(f"{key}\n")
                    outfile.write("************************************************\n")
                    outfile.write("\n*****************Decrypted Text*****************\n")
                    outfile.write(f"{plain_text}\n")
                    outfile.write("************************************************\n\n")


def encrypt(key, plaintext, vigenere_table):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    plaintext_table = []
    encrypted_message = []
    
    # Placeholder variables for the row and column
    i = 0
    j = 0
    
    # Use key as first row
    key_row = []
    while i < len(key):
        key_row.append(key[i])
        i += 1 # Increment column
    plaintext_table.append(key_row)
    
    character = 0 # Initialize character count
    while character < len(plaintext):
        row = [] # Initialize row
        i = 0 # Reinitilize i every loop
        while i < len(key) and character < len(plaintext):
            row.append(plaintext[character])
            character += 1 # Increment character count
            i += 1 # Increment column
        plaintext_table.append(row)
        j += 1 # Increment row
    
    character = 0
    key_index = 0
    
    while character < len(plaintext):
        plain_char = plaintext[character]
        
        # Get row index using the current key character
        row_index = vigenere_table[0].index(key[key_index % len(key)])
        
        # Get column index for the plaintext character
        column_index = vigenere_table[0].index(plain_char)
        
        # Encrypted character from the first row of the table
        encrypted_char = vigenere_table[row_index][column_index]
        encrypted_message.append(encrypted_char)
        
        character += 1
        key_index += 1
    
    return ''.join(encrypted_message)


def decrypt(key, ciphertext, vigenere_table):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    ciphertext_table = []
    decrypted_message = []
    
    # Placeholder variables for the row and column
    i = 0
    j = 0
    
    # Use key as first row
    key_row = []
    while i < len(key):
        key_row.append(key[i])
        i += 1 # Increment column
    ciphertext_table.append(key_row)
    
    character = 0 # Initialize character count
    while character < len(ciphertext):
        row = [] # Initialize row
        i = 0 # Reinitilize i every loop
        while i < len(key) and character < len(ciphertext):
            row.append(ciphertext[character])
            character += 1 # Increment character count
            i += 1 # Increment column
        ciphertext_table.append(row)
        j += 1 # Increment row
    
    character = 0
    key_index = 0
    
    while character < len(ciphertext):
        cipher_char = ciphertext[character]
        
        # Get row index using the current key character
        row_index = vigenere_table[0].index(key[key_index % len(key)])
        
        # Get column index for the ciphertext character
        column_index = vigenere_table[row_index].index(cipher_char)
        
        # Decrypted character from the first row of the table
        decrypted_char = vigenere_table[0][column_index]
        decrypted_message.append(decrypted_char)
        
        character += 1
        key_index += 1

    
    return ''.join(decrypted_message)


def display_menu():
    print()
    print(f"      Kryptos Encryption/Decryption Tool")
    print("************************************************")
    print("1. Encrypt Text Using Vigenere Table and Key")
    print("2. Encrypt Text Using Vigenere Table and Key List")
    print("3. Decrypt Text Using Vigenere Table and Key")
    print("4. Decrypt Text Using Vigenere Table and Key List")
    print("5. Exit Program")
    print("************************************************")


kryptos()

