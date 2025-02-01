#
# Lindsey Cary
# 2/1/25
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSales = 0.0

# Constants for the state and county tax rates
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Get the amount of the purchase.
purchase = float(input('Enter the amount of the purchase: '))

# Calculate the state sales tax.
stateTax = purchase * STATE_TAX_RATE

# Calculate the county sales tax.
countyTax = purchase * COUNTY_TAX_RATE

# Calculate the total tax.
totalTax = stateTax + countyTax

# Calculate the total of the sale.
totalSales = purchase + totalTax

# Print information about the sale.
print("Purchase Amount:$", format(purchase, ',.2f'))
print("State Tax: $", format(stateTax, ',.2f'))
print("County Tax: $", format(countyTax, ',.2f'))
print("Total Tax: $", format(totalTax, ',.2f'))
print("Sale Total: $", format(totalSales, ',.2f'))

# Ready for grading.

