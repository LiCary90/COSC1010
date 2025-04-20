#
# Lindsey Cary
# April 20, 2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables
    correctAnswers = 0
    incorrectAnswers = 0

    print("Welcome to the U.S. State Capital Quiz!")

    # Continue until user quits the game.
    print("Type 'quit' at any time to exit.\n")

    # Get a list of the states from the dictionary keys.
    states = list(capitals.keys())

    # Loop until user decides to quit.
    while True:
        # Randomly select a state
        state = random.choice(states)
        # Ask the user for the capital
        answer = input(f"What is the capital of {state}? ").strip()

        # Exit condition
        if answer.lower() == 'quit':
            break

        # Check the answer (case-insensitive)
        if answer.lower() == capitals[state].lower():
            print("Correct!\n")
            correctAnswers += 1
        else:
            print(f"Incorrect! The correct answer is {capitals[state]}.\n")
            incorrectAnswers += 1
        
    # Show final results.
    print("Thanks for playing!")
    print(f"Correct Answers: {correctAnswers}")
    print(f"Incorrect Answers: {incorrectAnswers}")

# Call the main function.
main()
