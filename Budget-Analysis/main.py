#
# Lindsey Cary
# 2/16/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# This program helps users track their expenses against a predefined monthly budget.
# The user enters a budget and then logs expenses until they are done.
# The program calculates wheather they are over or under budget and displays the result.

# Constants
EXIT_KEYWORD = 'done'   # Keyword to exit the expense input loop

# Initialize variables
budget = float(input("Enter your budget for the month: $")) # User-defined monthly budget
total_Expenses = 0.0    # Running total of expenses
expense = 0.0           # Stores individual expense amounts entered by the user
balance = 0.0           # Stores the final balance after calculations

# Loop to collect expenses until the user types 'done'.
while True:
    try:
        expense = input(f"Enter an expense amount (or type '{EXIT_KEYWORD}' to finish): ") # Prompt user for expense entry
        if expense.lower() == EXIT_KEYWORD:  # Check if user is finished entering expenses
            break
        expense = float(expense)  # Convert input to a float number
        if expense < 0:  # Ensure expenses are non-negative
            print("Please enter a non-negative expense.")
            continue
        total_Expenses += expense # Add the expense to the running total
    except ValueError:
        print("Invalid input. Please enter a valid number.") # Handle incorrect input

# Calculate remaining budget or overspending
balance = budget - total_Expenses   # Determine the difference between budget and expenses

# Display final budget status
if balance > 0:
    print(f"You are under budget by ${balance:.2f}.")   # Inform the user they are under budget
elif balance < 0:
    print(f"You are over budget by ${-balance:.2f}.")   # Inform the user they have overspent
else:
    print("You have exactly met your budget.")  # Inform the user they matched their budget exactly
