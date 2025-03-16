#
# Lindsey Cary
# March 15, 2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Define the constant for the file name
FILE_NAME = "numbers.txt"

# Variables
total = 0   # Keeps track of the sum of numbers
count = 0   # Stores how many numbers are read
file = None # Represents the file object (handled by 'with open')
line = ""   # Temporarily holds each line read from the file
number = 0  # Stores the integer value converted from each line
average = 0 # Stores the computed average value    

# Main function to read numbers from the file and calculate the average
def main():

# Open the file in read mode
    try:
        with open(FILE_NAME, "r") as file:  # 'with' ensures automatic file closure
            total = 0
            count = 0

            # Read and process each line in the file
            for line in file: 
                number = int(line.strip())  # Converts the line (string) to an integer after removing whitespace
                total += number # Add number to total sum
                count += 1  # Incremental count of numbers

            # Calculates the average (only if the lease one nubmer is present)
            if count > 0:
                average = total / count     # Compute average
                print(f"The average of the numbers in '{FILE_NAME}' is: {average:.2f}")    

            else:
                print(f"Error: The file '{FILE_NAME}' is empty.")

# Handles case where the file does not exist
    except FileNotFoundError:
        print(f"Error: The file '{FILE_NAME}' was not found. Please check the file location.")

# Handles case where the file contains non-numeric data
    except ValueError:
        print(f"Error: The file '{FILE_NAME}' contains invalid (non-integer) values. Please verify the file contents.")

# Call the main function to execute the program
main()

            