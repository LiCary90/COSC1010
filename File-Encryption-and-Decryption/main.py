#
# Lindsey Cary
# April 26, 2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Part 1

# Dictionary to map letters to symbols
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

def main():
    # Ask for the input file name
    input_name = input('Enter the name of the input file: ')

    try:
        with open(input_name, 'r') as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_name}' was not found.")
        return

    # Convert the text
    result = ''
    for ch in text:
        if ch in CODE:
            result += CODE[ch]
        else:
            result += ch  # Keep any characters not in the CODE dictionary as they are

    # Ask for the output file name
    output_name = input('Enter the name of the output file: ')

    with open(output_name, 'w') as output_file:
        output_file.write(result)

    print(f"Encryption complete! Encrypted text written to '{output_name}'.")

# Call the main function
main()