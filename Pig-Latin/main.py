#
# Lindsey Cary
# April 13, 2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Function to convert a single word to Pig Latin
def to_pig_latin(word):

    # If the word has only one letter, just add 'AY'
    if len(word) == 1:
        return word + "AY"
    else:
        # Move the first letter to the end and add 'AY'
        return word[1:] + word[0] + "AY"
    
# Main function
def main():
    # Prompt user for input
    sentence = input("Enter a sentence in English (use UPPERCASE): ")

    # Split the sentence into individual words
    words = sentence.split()

     # Convert each word using the Pig Latin Function
    pig_latin_words = []
    for word in words:
        pig_word = to_pig_latin(word)
        pig_latin_words.append(pig_word)

    # Join a display the Pig Latin Sentence
    pig_latin_sentence = ' '.join(pig_latin_words)
    print("\nPig Latin Version:")
    print(pig_latin_sentence)
    
# Call the main function to run the program
main()