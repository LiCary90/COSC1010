#
# Lindsey Cary
# April 6, 2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Import the random module to select random responses
import random

# Constants
FILENAME = "Magic-8-Ball/8_ball_responses.txt"

# Variables
responses = []  # List to hold all 8 ball responses
userInput = ""  # Variable to store the user's input

def main():
    # Open the file and read all responses into the list
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                responses.append(line.strip())  # Remove any newline characters
    except FileNotFoundError:
        print(f"Error: The file '{FILENAME}' could not be found.")
        return
    
    # Greet User
    print("Welcome to the Magic 8 Ball!")
    print("Ask any yes or no question, or type 'quit' to exit. \n")

    # Start the question-answer loop
    while True:
        userInput = input("What is your question?").strip()

        if userInput.lower() == 'quit':
            print("Goodbye!")
            break
        elif userInput == "":
            print("Please ask a valid question.")
        else:
            response = random.choice(responses)
            print("🎱", response, "\n")

# Call the main function to run the program
main()
