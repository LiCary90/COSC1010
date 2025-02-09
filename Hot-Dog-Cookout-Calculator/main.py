#
# Lindsey Cary
# 2/8/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local variables
numAttending = 0    # The number of people attending
numPerPerson = 0    # The number of hot dogs and buns per person
total = 0           # The total number of hot dogs and buns needed
minDogs = 0         # The minimum number of packages of hot dogs 
minBuns = 0         # The minimum number of packages of hot dog buns
leftoverDogs = 0    # The number of leftover hot dogs
leftoverBuns = 0    # The number of leftover hot dog buns

# Get the number of people attending the cookout from the user. 
numAttending = int(input("Enter the number of people attending the cookout: "))

# Get the number of hot dogs per person from the user.
numPerPerson = int(input("Enter the number of hot dogs each person will receive: "))

# Calculate the total number of hot dogs and buns needed.
total = numAttending * numPerPerson

# Calcualte the minimum number of packages of hot dogs needed.
minDogs = (total + HOT_DOGS_PER_PACKAGE -1) // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dogs.
if total > HOT_DOGS_PER_PACKAGE:
    print("More than one package of hot dogs is required.")
else:
    print("Only one package of hot dogs is required.")

# Calculate the number of leftover hot dogs. 
leftoverDogs = (minDogs * HOT_DOGS_PER_PACKAGE) - total

# Calcualte the min number of packages of hot dog buns needed.
minBuns = (total + BUNS_PER_PACKAGE -1) // BUNS_PER_PACKAGE

# Determine if the number of people attending is large enough to require more than one package of hot dog buns. 
if total > BUNS_PER_PACKAGE :
    print("More than one package of hot dog buns is required.")
else:
    print("only one package of hot dog buns is required")

# Calculate the number of leftover hot dog buns.
leftoverBuns = (minBuns * BUNS_PER_PACKAGE) - total

# Ensure leftovers are not negative.
leftoverDogs = max(0, leftoverDogs)
leftoverBuns = max(0, leftoverBuns)

# Display the results.
print("\nCookout Planning Results:")
print(f"Minimum hot dog packages required: {minDogs}")
print(f"Minimum hot dog bun packages required: {minBuns}")
print(f"Hot dogs left over: {leftoverDogs}")
print(f"Hot dog buns left over: {leftoverBuns}")

# Ready for grading.