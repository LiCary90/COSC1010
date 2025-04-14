#
# Lindsey Cary
# April 13, 2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Constants
VOWELS = ['a', 'e', 'i', 'o', 'u']

# Function: Returns the number of vowels in a string
def num_vowels(s):
    v_count = 0
    for ch in s:
        if ch.lower() in VOWELS:
            v_count += 1
    return v_count

# Function: Returns the number of consonants in a string
def num_consonants(s):
    c_count = 0
    for ch in s:
        if ch.isalpha() and ch.lower() not in VOWELS:
            c_count += 1
    return c_count
    
# Main Function
def main():
    user_str = input('Enter a string of characters: ')

    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')

# Call the main function
main()