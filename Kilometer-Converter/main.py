#
# Lindsey Cary
# 2/23/2025
# Kilometer Converter Programming Project
# COSC 1010
#
#  This program converts kilometers to miles.

# Constant for conversion
CONVERSION_FACTOR = 0.6214  # This value does not change

# The main function gets a distance in kilometers and calls the show_miles function to convert it.
def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)  # Fixed spacing

# The show_miles function converts the parameter km from kilometers to miles and displays the result.
def show_miles(km):  # Fixed inconsistent parameter name (KM → km)
    # Calculate miles.
    miles = km * CONVERSION_FACTOR  # Fixed incorrect variable reference (KM → km)

    # Display the miles.
    print(km, 'kilometers equals', f"{miles:.2f}", 'miles.')  # Formatting for readability

# Call the main function
main()
