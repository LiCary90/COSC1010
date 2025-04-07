#
# Lindsey Cary
# March 15, 2025
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Constants for the file name
FILE_NAME = 'Magic-8-ball/8_ball_responses.txt'

# Variables
total = 0   # Keeps track fo the sum of numbers
count = 0   # Stores how many numbers are read
file = None # Represents the file object (handled by 'with open')
line = ""   # Temporarily holds each line read from the file
number = 0  # Stores the integer value converted from each line
average = 0 # Stores the computed average value.

# Main function
def main():
    total = 0
    count = 0

    # Try to open the file for reading
    try:
        with open(FILE_NAME, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())  # Convert line from string to integer
                    total += number             # Add number to total
                    count += 1                  # Increment count of numbers

                # Handle the case where data in the file is not a valid integer
                except ValueError:
                    print(f"Warning: Skipping invalid data in file -> '{line.strip()}' (Not an integer)")

        # Check if count is greater than 0 before computing the average
        if count > 0:
            average = total / count
            print(f"The average of the numbers in {FILE_NAME} is: {average:.2f}")
        else:
            print(f"No valid numbers found in {FILE_NAME}.")

    # Handle case where the file is missing
    except FileNotFoundError:
        print(f"Error: The file '{FILE_NAME}' was not found.")
    
    #Handle input/output erros while assessing the file
    except IOError:
        print(f"Error: Problem reading the file '{FILE_NAME}'.")

# Call the main funciton
main()
