#
# Lindsey Cary
# 2/9/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lengthA = 0 # The length of rectangle A
widthA = 0  # The width of rectangle A
lengthB = 0 # The length of rectangle B
widthB = 0  # The width of rectangle B
areaA = 0   # The area of rectangle A
areaB = 0   # The area of rectangle B

# Get length A
lengthA = float(input("Enter the length of the first rectangle: "))

# Get width A
widthA = float(input("Enter the width of the first rectangle: "))

# Get length B
lengthB = float(input("Enter the length of the second rectangle: "))

# Get width B
widthB = float(input("Enter the width of the second rectangle: "))


# Calculate area A
areaA = lengthA * widthA

# Calculate area B
areaB =  lengthB * widthB

# Print area comparison using if-elif-else statements
if areaA > areaB:
    print("The first rectangle has the greater area")
elif areaB > areaA:
    print("The second rectangle has the greater area")
else:
    print("Both rectangles have the same area.")
