#
# Lindsey Cary
# March 15, 2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Constants
NUM_DIGITS = 7  # Defines the number of digits in the lottery number

# Varialbes
lotteryNumbers = [] # Stores the list of generated lottery digits
number = 0          # Stores each randomly generated digit before adding to the list
digit = 0           # Used in the loop to display each digit in the list

# Import the random module to generate random numbers
import random

# Main function to generate and display the lottery numbers.
def main():

    # Create and empty list to store the lottery numbers
    lotteryNumbers = []

    # Generate seven random digits (0-9) and store them in the list
    for _ in range(NUM_DIGITS):
        number = random.randint(0, 9)   # Generate a random number between 0 and 9
        lotteryNumbers.append(number)   # Append the number to the list

    # Display the genterated lottery number with spaces between each digit for readability
    print("Your lottery number is:", " ".join(map(str, lotteryNumbers)))

# Call the main function to execute the program
main()