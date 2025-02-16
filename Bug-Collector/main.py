#
# Lindsey Cary
# 2/16/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
bugs_Collected = 0 # Stores the number of bugs collected in each day
total_Bugs = 0 # Stores the total number of bugs collected over 7 days

# Number of days the bug collector collects bugs.
DAYS = 7

# Get number of bugs collected each day using a for loop.
for day in range(1, DAYS + 1):
    while True:
        try:
            bugs_Collected = int(input(f"Enter the number of bugs collected on day {day}: "))
            if bugs_Collected < 0:
                print("Please enter a non-negative number.")
                continue
            total_Bugs += bugs_Collected
            break
        except ValueError:
            print("Invalid iput. Please enter a whole number.")

# Display the total number of bugs collected.
print(f"Total number of bugs collected over {DAYS} days: {total_Bugs}")