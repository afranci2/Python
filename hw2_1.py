# Name: Anthony Francisco
# Date: 2/6/23
# Title: CSC 110 - Homework 2 - Programming in Python
# Description: This code calculates the discount for a sale amount entered by the user. 
# The code uses an if-elif-else statement to determine the discount rate based on the sale amount 
# and returns the final sale amount after applying the discount. 

# Get the sale amount from the user
sale_amount = float(input("Enter the amount of sale: "))

def calculate_discount(sale_amount):
    # Determine the discount rate based on the sale amount
    if sale_amount > 5000:
        return sale_amount * .45
    elif sale_amount > 3000:
        return sale_amount * .3
    elif sale_amount > 1000:
        return sale_amount * .15
    else:
        return sale_amount

# Calculate and print the final sale amount after applying the discount
print("The final sale amount is $ ", "{:,.2f}".format(calculate_discount(sale_amount)))
