#
# Lindsey Cary
# April 26, 2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Part 2

# Original encryption dictionary
CODE = {'A': '%', 'a': '9',
    'B': '@', 'b': '#',
    'C': '&', 'c': '1',
    'D': '$', 'd': '2',
    'E': '!', 'e': '3',
    'F': '*', 'f': '4',
    'G': '^', 'g': '5',
    'H': '~', 'h': '6',
    'I': '+', 'i': '7',
    'J': '=', 'j': '8',
    'K': '(', 'k': ')',
    'L': '[', 'l': ']',
    'M': '{', 'm': '}',
    'N': '<', 'n': '>',
    'O': '?', 'o': '/',
    'P': '|', 'p': '\\',
    'Q': '`', 'q': ';',
    'R': ':', 'r': '"',
    'S': ',', 's': '.',
    'T': '-', 't': '_',
    'U': '0', 'u': 'a',
    'V': 'b', 'v': 'c',
    'W': 'd', 'w': 'e',
    'X': 'f', 'x': 'g',
    'Y': 'h', 'y': 'i',
    'Z': 'j', 'z': 'k',
    ' ': ' '}

# Reverse the CODE dictionary for decryption
REVERSE_CODE = {v: k for k, v in CODE.items()}

def decrypt_file():
    # Ask for the input encrypted file name
    input_name = input('Enter the name of the encrypted file: ')

    try:
        with open(input_name, 'r') as input_file:
            encrypted_text = input_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_name}' was not found.")
        return

    # Decrypt the text
    decrypted_text = ''
    for ch in encrypted_text:
        if ch in REVERSE_CODE:
            decrypted_text += REVERSE_CODE[ch]
        else:
            decrypted_text += ch  # Leave any unknown characters unchanged

    # Display the decrypted text
    print("\nDecrypted Text:\n")
    print(decrypted_text)

# Call the function
decrypt_file()