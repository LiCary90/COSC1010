#
# Lindsey Cary
# March 16, 2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Define a constant for the file name
FILE_NAME = "numbers.txt"     # This is the file that contains the numbers

# Main fuction to red and display numbers from the file
def main():
 
    # Open the file in read mode
    try:
        with open(FILE_NAME, "r") as file:     # 'with ensure the file is properly closed after use
            for line in file:                  # Loop through each line in the file
                number = int(line.strip())     # Convert the line (string) to an integer after stripping whitespace
                print(number)                  # Print the number to the console

# Handle the case where the file does not exist
    except FileNotFoundError:  
        print(f"Error: The file '{FILE_NAME}' was not found. Please check the file location.")  

# Handle the case where the file contains non-numeric data
    except ValueError:
        print(f"Error: The file '{FILE_NAME}' contains not-integer values. Please verify file contents.")

# Call the main function to execute the program.
main()

