#
# Lindsey Cary
# 2/23/25
# Feet to Inches Programming Project
# COSC 1010
#
# This program converts a given number of feet to inches.
#


# Constant for the number of inches per foot. 
INCHES_PER_FOOT = 12    # 1 foot = 12 inches

# main function
def main ():

    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches and display the result.
    print(f"{feet} feet equals {feet_to_inches(feet)} inches.")


# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    
    return feet * INCHES_PER_FOOT

# Call the main function.
main ()

